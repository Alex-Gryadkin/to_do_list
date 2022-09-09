from application import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_descr = db.Column(db.String(300))
    status = db.Column(db.String(30), index=True)

    def __repr__(self):
        return f'<Task #{self.id} - {self.status}: {self.task_descr}>'