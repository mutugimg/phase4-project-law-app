from flask import Flask, make_response, request
from flask_migrate import Migrate
# from flask_restful import API, Resource
# from flask_session import Session
from models import User, Lawyer, Issue, Appointment, db
# from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///law.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "<h1> Welcome to our Database </h1>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)