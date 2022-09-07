from flask import render_template
from application import app


@app.route('/')
@app.route('/index')
def index():
    to_dos = [
        {'number': 1,
         'task_name': 'Открыть FLASK',
         'status': 'Done'
         },
        {
         'number': 2,
         'task_name': 'Сгореть к хуям',
         'status': 'In Progress'
        }
    ]
    return render_template('index.html', to_dos=to_dos)