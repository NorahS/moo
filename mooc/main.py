import webapp2 ,jinja2,os

import addC,user,pages 


class ajax(addC.Handler.Handler):
	def get(self):
		self.render("ajax.html")
	def post(self):
		self.render("ajax.html")

PAGE_RE = r'((?:[a-zA-Z0-9_-]+/?)*)'
PAGE_R =r'(/(?:[a-zA-Z0-9_-]+/?)*)'

application = webapp2.WSGIApplication([('/login',user.Login),('/logout',user.Logout),('/page'+PAGE_R,pages.Page),('/search'+PAGE_RE,addC.Search),('/',ajax),('/signup',user.Signup),('/us',addC.add)],debug = True) 


