from . import create_app
from server.models.models import Reception ,Donor ,Bloodbank,Blood
from sqlalchemy.exc import SQLAlchemyError
from server.controllers.Donor_controller import get,get_id,delete_donor,create_donor
from server.controllers.Blood_controller import get_blood,get_bloodId
from server.controllers.Bloodbank_contrller import get_bloodbank
from server.controllers.Reception_controller import get_recept,get_receptId


app=create_app()

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





@app.route('/')
def home():
    return 'welcome home'
@app.route('/receptions',methods=['GET'])
def get_reception():
    return get_recept()
@app.route('/receptions/<int:id>',methods=['GET'])
def get_reception_byId(id):
    return get_receptId(id)
@app.route('/donor',methods=['POST'])
def form_donor():
    return create_donor()
@app.route('/donor',methods=['GET'])
def get_donor():
    return get()
@app.route('/donor/<int:D_id>',methods=['DELETE'])
def remove_donor(D_id):
    return delete_donor(D_id)
@app.route('/donor/<int:D_id>',methods=['GET'])
def get_byId(D_id):
    return get_id(D_id)
@app.route('/blood',methods=['GET'])
def list_blood():
    return get_blood()
@app.route('/blood/<int:D_id>',methods=['GET'])
def list_byId(D_id):
    return get_bloodId(D_id)
@app.route('/bloodbank',methods=['GET'])
def list_bloodbank():
    return get_bloodbank()
# @app.route('/bloodbank/<int:b_group>',methods=['GET'])
# def list_bloodbankId(b_group):
#     return get_bloodbankId(b_group)







if __name__=='__main__':
    app.run(debug=True)
