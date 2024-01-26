from flask import  jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError
import logging
from server.models.models import Bloodbank


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def get_bloodbank():   
    try:
        return jsonify([n.serialize() for n in Bloodbank.query.all()]), 200
    except SQLAlchemyError as e:
        return handle_error(e, 500)
def get_bloodbankId(b_group):
    try:    
        donor = Bloodbank.query.filter(b_group==b_group).first()
        return (jsonify(donor.serialize()),200) 
    except SQLAlchemyError as e:
        return handle_error(e, 500)    
