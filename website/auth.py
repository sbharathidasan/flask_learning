from flask import Blueprint,render_template,request,flash
import psycopg2
auth=Blueprint('auth',__name__)
@auth.route('/login',methods=["GET","POST"])
def signin():
  if request.method=="POST":
    email=request.form.get("email")
    fname=request.form.get("FirstName")
    password=request.form.get("password")
    return "hey"+fname
  return render_template("signin.html")

@auth.route('/logout',methods=["GET","POST"])
def signout():
  return render_template("signout.html")

@auth.route('/signup',methods=["GET","POST"])
def signup():
  if request.method=="POST":
    email=request.form.get("email")
    fname=request.form.get("FirstName")
    password=request.form.get("password")
    cnfpassword=request.form.get("password2")
    if (len(email)<4):
      flash("Email mustbe greater than 4 characters",category="error")
    elif len(fname)<2:
      flash("username must be greater then 1 character",category="error")
    elif cnfpassword!=password:
      flash("password mismatch",category="error")
    elif len(password)<8:
      flash("password must be at least 7 characters",category="error")
    else:
      flash("account created successfully",category="success")
  return render_template("signup.html")
  

  