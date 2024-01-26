from .. import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class Reception(db.Model,SerializerMixin):
    
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))

class Donor(db.Model,SerializerMixin):
    
    D_id=db.Column(db.Integer(), primary_key=True)
    Dname=db.Column(db.String(100))
    Demail=db.Column(db.String(100))
    sex=db.Column(db.String(100))    
    address=db.Column(db.String(100)) 
    age=db.Column(db.Integer())
    weight=db.Column(db.Integer())
    donor_Date= db.Column(db.DateTime,default=datetime.utcnow)   

    blood1= db.relationship("Blood", backref="donors")

    def serialize(self):
        return {
            'D_id': self.D_id,
            'Dname': self.Dname,
            'sex': self.sex,
            'address': self.address,
            'age': self.age,
            'weight': self.weight,
            'donor_Date': self.donor_Date
        }

class Blood(db.Model,SerializerMixin):
    
    b_code=db.Column(db.Integer(), primary_key=True)
    D_id=db.Column(db.Integer(), db.ForeignKey('donor.D_id'))
    packets=db.Column(db.Integer())
    B_group=db.Column(db.String(100))

    def serialize(self):
        return {
            'D_id': self.D_id,
            'b_code': self.b_code,
            'packets': self.packets,
            'B_group': self.B_group
        }

class Bloodbank(db.Model,SerializerMixin):
    
    b_group=db.Column(db.String(100),primary_key=True)
    total_packets=db.Column(db.Integer())

    def serialize(self):
        return {
            'b_group': self.b_group,
            'total_packets': self.total_packets
        }


