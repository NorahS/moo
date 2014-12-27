import Handler , coursesdb, cached

class add(Handler.Handler):
	def get(self):
		self.render("add_form.html")
	def post(self):
		name =self.request.get("Name") 
		course1 = self.request.get("School")
		instructor = self.request.get("Instructor")
	#	rate = self.request.get("Rate")
	#	level= self.request.get("Level")
		subject= self.request.get("Subject")
		platform= self.request.get("Platform")
	#	date= self.request.get("Date")
	#	img = self.request.get("img")

		if  cached.cached(name) :
			ratel =[0 for i in range(10)]
			ratel[int(rate)-1]+=1 		
		#	course = coursesdb.Courses(key_name=name, Platform = platform,Name=name,School=course1,Rate=ratel,Instructor= instructor, Level = level, Subject=subject,Date=date, Img=img)
                        
                        course = coursesdb.Courses(key_name=name, Platform = platform,Name=name,School=course1)


			course.put()
                        course.cache(instructor,course1,subject,name)
			cached.cache(name,course)
			self.render("add_form.html",post="Done")
		else:
			self.render("add_form.html", post =cached.cached(name))
		

class Search(Handler.Handler):
        def get(self,p):
                q = self.request.get("q")
                if q :
                        # the courses are already cached so we dont have to query 
                   #     result =coursesdb.db.GqlQuery("SELECT * FROM Courses where Name= :1",q)

                        # lets check the memcach
                        result =cached.lookup(q)
                        if result == None:
                                result =coursesdb.lookup(q)
                                if result != None:
                                        ob = result
                        else :
                                ob = q
                                
                else :
                        result= False
       
                if result :
                        self.render("reuslt.html", result = resut)
                     #   self.redirect("/page/"+ob)
                         #self.render("search.html",post = result)
                else: 
                        self.render("search.html",post = result)
c
