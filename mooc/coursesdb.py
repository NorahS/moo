
from google.appengine.ext import db 

class Courses(db.Model):
	Name = db.StringProperty(required= True)
	School = db.StringProperty(required = True)
	Instructor= db.StringProperty()
	Platform = db.StringProperty(required = True)
	Rate = db.IntegerProperty()
	Level= db.StringProperty()
	Subject = db.StringProperty()
	Date = db.DateProperty() 
	Link = db.TextProperty()
	Img = db.BlobProperty()
