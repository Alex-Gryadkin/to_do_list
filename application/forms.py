from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewTask(FlaskForm):
    task_descr = StringField('Task_description', validators=[DataRequired()])
    submit = SubmitField('Add task')


