
from google.appengine.ext import db 

Instructors ={}
Schools ={}
Subjects ={}
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
        def cash(self,ins,school , sub, course):
                 f = Instructors.get(ins ,0)
                if f == 0:
                       Instructors[ins] =[]
                Instructors[ins].append(course)
                f = Schools.get(school,0)
                if f = 0 :
                        Schools[school]=[]
                Schools[school].append(cousre)
                f = Subjects.get(sub,0)
                if f ==0:
                        Subjects[sub] =[]
                Subjects[sub].append(course)
                
