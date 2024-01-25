from . import create_app,db
from flask_restful import Api, Resource
from flask import  jsonify, make_response, request
from server.models.models import Reception ,Donor ,Bloodbank,Blood
import logging
from sqlalchemy.exc import SQLAlchemyError



app=create_app()
api = Api(app)

# from datetime import datetime
# # from . import db
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


# db=SQLAlchemy()

# app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///donation.db'

# db.init_app(app)
# migrate=Migrate(app,db)

logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code


@app.route('/')
def home():
    return 'welcome home'

class Reception_details(Resource):
    def get(self):
        try:
            receptions= Reception.query.all()
            response=[reception.to_dict() for reception in receptions]
            return make_response(jsonify(response),200)
        except SQLAlchemyError as e:
            return handle_error(e,500)

class Reception_byId(Resource):
    def get(self,id):
        reception= Reception.query.filter(id==id).first()
        return make_response(jsonify(reception.to_dict()),200)

    def delete(self,id):
        try:
            reception= Reception.query.filter(id==id).first()
            db.session.delete(reception)
            db.commit()
        except SQLAlchemyError as e:
            return handle_error(e,500)
     

api.add_resource(Reception_details,'/receptions')
api.add_resource(Reception_byId,'/receptions/<int:id>')


if __name__=='__main__':
    app.run(debug=True)
