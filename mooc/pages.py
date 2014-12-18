import Handler, cached, user

class Page(Handler.Handler):
    def get(self,ob):
        ob = cached.lookup(ob[1:])
        self.render("page.html", ob = ob)
    def post(self):
        add = self.request.get("add")
        name = self.request.get("Name")
        rate = self.request.get("rate")
        if add:
            cookie =self.request.headers['user']
            user1 =user.logged[cookie]
            user1.courses.append(name) 
        # i have to do the rating thing

