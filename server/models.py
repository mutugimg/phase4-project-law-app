from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String,nullable=False)
    last_name = db.Column(db.String,nullable=False)
    user_name = db.Column(db.String, unique=True,nullable=False)
    email = db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String, unique=True,nullable=False)
    created_at = db.Column(db.DateTime, server_default = db.func.now)
    updated_at = db.Column(db.DateTime, onupdate = db.func.now)

    appointment=db.relationship('Appointment', back_populates='user')

    

    def __repr__(self):
        return f'Username:{self.user_name}, email address:{self.email}'
    

class Lawyer(db.Model,SerializerMixin):
    __tablename__ = 'lawyers'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    specialty = db.Column(db.String)
    email = db.Column(db.String, unique=True,nullable=False)
    contact = db.Column(db.String, unique=True,nullable=False)

    appointment=db.relationship('Appointment', back_populates='lawyer')

    def __repr__(self):
        return f'Fullname:{self.full_name}, email address:{self.email}, contact:{self.contact}'
    
class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    issue = db.Column(db.String,nullable=False)
    
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    # lawyer_id = db.Column(db.Integer, db.ForeignKey("lawyers.id"))

    def __repr__(self):
        return f'Issue:{self.issue}'
    
class Appointment(db.Model,SerializerMixin):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    lawyer_id = db.Column(db.Integer, db.ForeignKey("lawyers.id"))
    issue_id = db.Column(db.Integer, db.ForeignKey("issues.id"))
    appointment_date = db.Column(db.DateTime, nullable = False)

    issue = db.relationship('Issue')
    lawyer = db.relationship('Lawyer',back_populates='appointment')
    user = db.relationship('User',back_populates='appointment')
    
    def __repr__(self):
        return f'Issue:{self.issue}'



