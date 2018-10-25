from app import db
from models import BlogPost


db.create_all()

db.session.add(BlogPost("good", "super good"))
db.session.add(BlogPost("gre", "super gre"))

db.session.commit()