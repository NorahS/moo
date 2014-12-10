import webapp2 ,jinja2,os

import addC 

class ajax(addC.Handler.Handler):
	def get(self):
		self.render("ajax.html")
	def post(self):
		self.render("ajax.html")
application = webapp2.WSGIApplication([('/',ajax),('/us',addC.add)],debug = True) 


