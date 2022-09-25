from application import db
from flask import render_template, redirect, url_for
from application import app
from application.forms import NewTask
from application.models import Task
from application.models import Status


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NewTask()

    if form.validate_on_submit():
        task = Task(task_descr=form.task_descr.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    to_dos = Task.query.all()
    return render_template('index.html', to_dos=to_dos, form=form)


@app.route('/delete/<int:task_id>')
def delete(task_id):
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/change/<int:task_id>')
def change(task_id):
    task = Task.query.filter_by(id=task_id).first()
    print(task.status)

    if task.status == Status.to_do:
        task.status = Status.in_progress

    elif task.status == Status.in_progress:
        task.status = Status.done

    else:
        task.status = Status.to_do

    db.session.commit()
    return redirect(url_for('index'))
