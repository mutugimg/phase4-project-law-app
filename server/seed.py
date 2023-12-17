from models import Issue,User,db, Appointment, Lawyer
import random
from random import randint
from app import app
import json
from faker import Faker

fake=Faker()

with app.app_context():

    db.session.query(User).delete()
    db.session.query(Issue).delete()
    db.session.query(Lawyer).delete()
    db.session.query(Appointment).delete()



    users = []
    for _ in range(20):
        user = User(first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    user_name=fake.user_name(),
                    email=fake.email(),
                    password=fake.password())
        
        users.append(user)
    db.session.add_all(users)
    db.session.commit()
        

    issues=[]
    cases=['compliance', 'criminal law','torts','land registration', 'corporate law','divorce']
    for case in cases:
        issue=Issue(
            issue=case)
        issues.append(issue)
    db.session.add_all(issues)
    db.session.commit()

    lawyers = []
    for case in cases:
        lawyer = Lawyer(full_name=fake.name(),
                    specialty=case,
                    email=fake.email(),
                    contact=fake.phone_number())
        
        lawyers.append(lawyer)
    db.session.add_all(lawyers)
    db.session.commit()

    appointments = []
    for _ in range(20):
        user = fake.random_element(User.query.all())
        lawyer = fake.random_element(Lawyer.query.all())
        issue = fake.random_element(Issue.query.all())


        appointment = Appointment(
            user_id=user.id,
            lawyer_id=lawyer.id,
            issue_id=issue.id,
            appointment_date=fake.date_time_this_month())
        appointments.append(appointment)

        db.session.add_all(appointments)
    db.session.commit()
    
    # with app.app_context():
        # appointments = Appointment.query.all()

    # for appointment in appointments:
    print(appointment)
    print(f"User: {appointment.user.first_name} {appointment.user.last_name}, Lawyer: {appointment.lawyer.full_name}, Issue: {appointment.issue.issue}")


    

