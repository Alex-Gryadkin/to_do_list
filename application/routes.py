from application import db
from flask import render_template, redirect, url_for
from application import app
from application.forms import NewTask, LoginForm
from application.models import Task
from application.models import Status


@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Alex Gryadkin'}
    form = NewTask()

    if form.validate_on_submit():
        task = Task(task_descr=form.task_descr.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    to_dos = Task.query.all()
    return render_template('index.html', to_dos=to_dos, form=form, user=user)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/change/<int:task_id>')
def change(task_id):
    task = Task.query.get(task_id)

    task.status = Status.in_progress if task.status == Status.to_do \
        else Status.done if task.status == Status.in_progress \
        else Status.to_do

    db.session.commit()
    return redirect(url_for('index'))
