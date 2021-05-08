from app import db
from models import Pet

db.drop_all()
db.create_all()

a = Pet(name="bloop", species="golden", age='4', notes='friendly')
b = Pet(name="cookie", species="hound", age='1', notes='puppy')
c = Pet(name="bear", species="labrador", age='2', notes='friendly')
d = Pet(name="mercy", species="Chihuahua", age='1', notes='loud')
e = Pet(name="coco", species="hound", age='2', notes='vaccinated')

db.session.add_all([a,b,c,d,e])
db.session.commit()
