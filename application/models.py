from application import db
import enum


class Status(enum.Enum):
    to_do = "To do"
    in_progress = "In progress"
    done = "Done"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_descr = db.Column(db.String(300))
    status = db.Column(db.Enum(Status), default=Status.to_do)

    def __repr__(self):
        return f'<Task #{self.id} - {self.status}: {self.task_descr}>'