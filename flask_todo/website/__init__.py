from flask import Flask,render_template,request

def todoapp():
  app=Flask(__name__)
  todo_list = []

  @app.route('/', methods=['GET', 'POST'])
  def index():
    if request.method == 'POST':
        todo_list.append(request.form['todo'])

    return render_template('todo.html', todo_list=todo_list)
  return app

