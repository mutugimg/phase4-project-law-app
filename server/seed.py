from models import Issue,User,db
from app import app


with app.app_context():
    db.session.query(User).delete()
    db.session.query(Issue).delete()

    db.session.commit()

    user1=User(
        first_name="Mark",
        last_name="Mutugi",
        user_name="MMG",
        email="mmg@gmail.com",
        password="12345",

    )
    db.session.add(user1)
    db.session.commit()
     
    issue1=Issue(
        issue='compliance'
    )
    db.session.add(issue1)
    db.session.commit()