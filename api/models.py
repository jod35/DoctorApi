from api.routes import db


class Patient(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    fname=db.Column(db.String(25),nullable=False)
    lname=db.Column(db.String(25),nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    sickness=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return  "{}".format(self.fname)