from google.appengine.ext import db

class Users(db.Model):
	username = db.StringProperty(required = True)
	password = db.StringProperty(required = True)
	email = db.StringProperty( required = True)
        courses = list()
        img = db.BlobProperty()
	rated= list()


	
	
