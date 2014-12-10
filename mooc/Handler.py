import os , jinja2,webapp2

tamplet_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader= jinja2.FileSystemLoader(tamplet_dir),autoescape = True)

class Handler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)
	def render(self, template,**a):
		t= jinja_env.get_template(template)
		self.write(t.render(a))


