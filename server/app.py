from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db=SQLAlchemy()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///donation.db'

db.init_app(app)
migrate = Migrate(app, db)


class Reception(db.Model):
    
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))

class Donor(db.Model):
    
    D_id=db.Column(db.Integer(), primary_key=True)
    Dname=db.Column(db.String(100))
    Demail=db.Column(db.String(100))
    sex=db.Column(db.String(100))    
    address=db.Column(db.String(100)) 
    age=db.Column(db.Integer())
    weight=db.Column(db.Integer())
    donor_Date= db.Column(db.DateTime,default=datetime.utcnow)   


class Blood(db.Model):
    
    b_code=db.Column(db.Integer(), primary_key=True)
    D_id=db.Column(db.Integer())
    packets=db.Column(db.Integer())
    B_group=db.Column(db.String(100))

class Bloodbank(db.Model):
    
    b_group=db.Column(db.String(100),primary_key=True)
    total_packets=db.Column(db.Integer())


@app.route('/')
def home():
    return 'welcome home'





if __name__=='__main__':
    app.run(debug=True)
