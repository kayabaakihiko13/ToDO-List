from applications import app
from flask import render_template,request,redirect,url_for
from applications.models import *


@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template('index.html',todo_list=todo_list)

@app.route('/add',methods=["POST"])
def add():
    try:
        title=request.form.get("title")
        new_todo=Todo(title=title,status=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("home"))
    except :
        return ("maaf database tidak masuk")
        
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    todo.status=not todo.status
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))
