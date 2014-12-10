import Handler , coursesdb, cached

class add(Handler.Handler):
	def get(self):
		self.render("add_form.html")
	def post(self):
		name =self.request.get("Name") 
		course = self.request.get("School")
		instructor = self.request.get("Instructor")
		rate = self.request.get("Rate")
		level= self.request.get("Level")
		subject= self.request.get("Subject")
		platform= self.request.get("Platform")
		date= self.request.get("Date")
		img = self.request.get("img")

		if  cached.cached(name) :		
		#	course = coursesdb.Courses(key_name=name, Platform = platform,Name=name,School=course,Rate=int(rate),Instructor= instructor, Level = level, Subject=subject,"""Date=date,""" Img=img)
			course = coursesdb.Courses(key_name=name, Platform = platform,Name=name,School=course,Rate=int(rate))		
			course.put()
			cached.cache(name,course)
			self.render("add_form.html",post="Done")
		else:
			self.render("add_form.html", post =cached.cached(name))
		