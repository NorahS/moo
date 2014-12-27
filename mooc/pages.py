import Handler, cached, user

class Page(Handler.Handler):
    def get(self,ob):
        ob = cached.lookup(ob[1:])
        self.render("page.html", ob = ob)
    def post(self):
        add = self.request.get("add")
        name = self.request.get("Name")
        rate = self.request.get("rate")
 	ob=self.request.get("ob")
        cookie =self.request.headers['user']
        user1 =user.logged[cookie]
	if add:        
		user1.courses.append(name) 
        # i have to do the rating thing
	if rate:
		if name in user1.rated:
			pass
		else:
			user1.rated.append(name)
			ob = cashed.lookup(ob)
			ob.rate[int(rate)-1]+=1

		
