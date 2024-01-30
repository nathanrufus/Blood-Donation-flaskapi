from flask import  jsonify, make_response, request
from sqlalchemy.exc import SQLAlchemyError
import logging
from server.models.models import Donor
from server import db


logging.basicConfig(level=logging.INFO)

def handle_error(e, status_code):
    logging.error(str(e))
    return jsonify({'error' : str(e)}), status_code

def create_donor():
    try:
        data = request.get_json()
        if 'Dname' not in data or 'Demail' not in data or 'sex' not in data or 'address' not in data or 'age' not in data or 'weight' not in data:
            return handle_error('Missing data fields', 400)
        new_donor=Donor(Dname=data['Dname'],Demail=data['Demail'],sex=data['sex'],address=data['address'],age=data['age'],weight=data['weight'])
        db.session.add(new_donor)
        db.session.commit()
        logging.info(jsonify(new_donor.serialize()))
        return jsonify(new_donor.serialize()), 201
    except SQLAlchemyError as e:
       return handle_error(e,500)    


def get():   
    try:
        donors = Donor.query.all()
        return jsonify([n.serialize() for n in donors]), 200
    except SQLAlchemyError as e:
        return handle_error(e, 500)
def get_id(D_id):
    try:    
        donor = Donor.query.filter(D_id==D_id).first()
        return (jsonify(donor.serialize()),200) 
    except SQLAlchemyError as e:
        return handle_error(e, 500)
def delete_donor(D_id):
        try:
            reception= Donor.query.filter(D_id==D_id).first()
            db.session.delete(reception)
            db.session.commit()
            return make_response(jsonify(reception.serialize()),200)
        except SQLAlchemyError as e:
            return handle_error(e,500)
    