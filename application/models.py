from application import db

class Summary(db.Model):
    __tablename__ = 'Summary'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, index=False, unique=False)

class Projects(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, index=False, unique=False)

class Whoami(db.Model):
    __tablename__ = 'Whoami'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, index=False, unique=False)

    def __init__(self, details):
        self.details = details

    def __repr__(self):
        return '<Details %r>' % self.details

class Education(db.Model):
    __tablename__ = 'Education'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, index=False, unique=False)

class About(db.Model):
    __tablename__ = 'About'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.Text, index=False, unique=False)

class Experience(db.Model):
    __tablename__ = 'Experience'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(45), index=True, unique=False)
    jobtitle = db.Column(db.String(45), index=False, unique=False)
    when = db.Column(db.String(45), index=True, unique=False)
    details = db.Column(db.Text, index=False, unique=False)
