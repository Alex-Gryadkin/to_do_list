from application import db
from flask import render_template, redirect, url_for
from application import app
from application.forms import NewTask
from application.models import Task


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