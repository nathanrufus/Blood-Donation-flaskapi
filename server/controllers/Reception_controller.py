from flask import  jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError
import logging
from server.models.models import Reception
from server import db


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def get_recept():   
    try:
        receptions= Reception.query.all()
        response=[reception.to_dict() for reception in receptions]
        return make_response(jsonify(response),200)
    except SQLAlchemyError as e:
        return handle_error(e,500)
def get_receptId(id):
    try:    
        reception= Reception.query.filter(id==id).first()
        return make_response(jsonify(reception.to_dict()),200)
    except SQLAlchemyError as e:
        return handle_error(e, 500)    
def delete_recept(id):
        try:
            reception= Reception.query.filter(id==id).first()
            db.session.delete(reception)
            db.commit()
        except SQLAlchemyError as e:
            return handle_error(e,500)
        
def update_recept(id):
        try:
            reception= Reception.query.filter(id==id).first()
            data=request.get_json()
            for attr in data:
                setattr(attr ,reception ,data[attr])
            db.session.add_all(reception)   
            db.commit() 
            return make_response(jsonify(reception),200)

        except SQLAlchemyError as e:
            return handle_error(e,500)  
