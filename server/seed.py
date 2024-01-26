from random import choice as rc
from app import app ,db,Donor
# from server.models.models import Donor
from faker import Faker

fake=Faker()

with app.app_context():
   # #  Reception.query.delete()
   #  for _ in range(20):
   #      reception= []
   #      new_reception=Reception(
   #         name=fake.name(),
   #         email=fake.email(),
   #         password=fake.password() 
   #      )
   #      reception.append(new_reception)

   #      db.session.add_all(reception)
   #      db.session.commit()

    for _ in range(20):
      #   Donor.query.delete()
        donor= []
        sex_val=['M','F']
        d_age = [60,55,67,56,43,24,58,98,67,56,23,43]
        new_donor=Donor(
           Dname=fake.name(),
           Demail=fake.email(),
           sex=rc(sex_val),
           address=fake.address(),
           age=rc(d_age),
           weight=rc(d_age)
        )
        donor.append(new_donor)

        db.session.add_all(donor)
        db.session.commit()


   #  for _ in range(20):
   #      blood= []
   #      packets_r = [6,5,6,5,4,2,8,9,6]
   #      d_id=[1,2,3,4,5,7,8,9]
   #      b_group=['A','B','O']
   #      my_donor=Blood(
   #         D_id=rc(d_id),
   #         packets=rc(packets_r),
   #         B_group=rc(b_group)
   #      )
   #      blood.append(my_donor)

   #      db.session.add_all(blood)
   #      db.session.commit()    

    
   #  for _ in range(10):
   #      bloodbank= []
        
   #      b_group=['A','B','O']
   #      my_donor=Bloodbank(
        
   #         b_group=rc(b_group)
   #      )
   #      bloodbank.append(my_donor)

   #      db.session.add_all(bloodbank)
   #      db.session.commit()        