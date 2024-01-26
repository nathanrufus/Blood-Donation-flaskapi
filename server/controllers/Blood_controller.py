from flask import  jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError
import logging
from server.models.models import Blood


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def get_blood():   
    try:
        return jsonify([n.serialize() for n in Blood.query.all()]), 200
    except SQLAlchemyError as e:
        return handle_error(e, 500)
def get_bloodId(D_id):
    try:    
        donor = Blood.query.filter(D_id==D_id).first()
        return (jsonify(donor.serialize()),200) 
    except SQLAlchemyError as e:
        return handle_error(e, 500)    
