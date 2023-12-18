from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
# from flask_session import Session
from models import User, Lawyer, Issue, Appointment, db
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///law.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)

class Index(Resource):
    try:
        def get(self):
            response_dict = {
                "index" : "Welcome to our Law App Database"
            }
            response = make_response(
                jsonify(response_dict),
                200,
            )

            return response
        
    except Exception as e:
        print (e)
    
api.add_resource(Index, "/")

class Users(Resource):
    def get(self):
        response_dict_list = [user.to_dict() for user in User.query.all()]
        
        response = make_response(
            jsonify(response_dict_list),
            200
        )

        return response
    
    def post(self):
        data = request.get_json()
        new_record = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            user_name=data["user_name"],
            email=data["email"],
            password=data["password"]
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            jsonify(response_dict),201
        )

        return response
    
api.add_resource(Users,'/users')

class Lawyers(Resource):
    def get(self):
        response_dict_list = [lawyer.to_dict() for lawyer in Lawyer.query.all()]
        
        response = make_response(
            jsonify(response_dict_list),
            200
        )

        return response
    
    def post(self):
        data = request.get_json()
        new_record = Lawyer(
            full_name=data["full_name"],
            specialty=data["specialty"],
            email=data["email"],
            contact=data["contact"]
        )

        db.session.add(new_record)
        db.session.commit()

        response_dict = new_record.to_dict()

        response = make_response(
            jsonify(response_dict),201
        )

        return response
    
api.add_resource(Lawyers, "/lawyers")

class UserByID(Resource):

    def get(self,id):
        response_dict = User.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(response_dict),200
        )

        return response

        
    def patch(self,id):
        record = User.query.filter_by(id=id).first()
        for attr in request.get_json():
            setattr(record, attr, request.get_json()[attr])
            db.session.commit()

        response_dict = record.to_dict()

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response
    
    def delete(self,id):
        record = User.query.filter_by(id=id).first()
        
        db.session.delete(record)
        db.session.commit()

        response_dict = {"message": "record succesfully deleted"}

        response = make_response(
            jsonify(response_dict),
            200
        )

        return response

api.add_resource(UserByID,"/users/<int:id>")



if __name__ == '__main__':
    app.run(port=5555, debug=True)