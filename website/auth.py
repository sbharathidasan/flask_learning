from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User 
from flask_login import login_user,login_required,logout_user,current_user
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth=Blueprint('auth',__name__)
@auth.route('/login',methods=["GET","POST"])
def signin():
  if request.method=="POST":
    email=request.form.get("email")
    password=request.form.get("password")
    user=User.query.filter_by(email=email).first()
    if user:
      if check_password_hash(user.password,password):
        flash("you are signed-in",category='success')
        login_user(user,remember=True)
        return redirect(url_for('views.home'))
      else:
        flash("password is incorrect",category="error")
    else:
      flash("Email does not exist,Please sign-up",category='error')
  return render_template("signin.html")

@auth.route('/logout',methods=["GET","POST"])
@login_required
def signout():
  logout_user()
  return redirect(url_for('auth.signin'))

@auth.route('/signup',methods=["GET","POST"])
def signup():
  if request.method=="POST":
    email=request.form.get("email")
    fname=request.form.get("FirstName")
    password=request.form.get("password")
    cnfpassword=request.form.get("password2")
    user=User.query.filter_by(email=email).first()
    if user:
      flash("Email already exist",category="error") 
    elif (len(email)<4):
      flash("Email mustbe greater than 4 characters",category="error")
    elif len(fname)<2:
      flash("username must be greater then 1 character",category="error")
    elif cnfpassword!=password:
      flash("password mismatch",category="error")
    elif len(password)<8:
      flash("password must be at least 7 characters",category="error")
    else:
      new_user=User(email=email,first_name=fname,password=generate_password_hash(password,method='pbkdf2:sha256'))
      db.create_all()
      db.session.add(new_user)
      db.session.commit()
      login_user(user,remember=True)
      flash("account created successfully",category="success")
      return redirect(url_for('views.home'))
  return render_template("signup.html")
  

  