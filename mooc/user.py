import Handler,usersdb ,userfun

class Signup(Handler.Handler):
	def get(self):
		self.render("signup_form.html")
	def post(self):
		username = self.request.get("username")
		email = self.request.get("email")
		password = self.request.get("password")
		conf = self.request.get("conf")

		error=" "
		user = usersdb.Users.all().filter("username =", username).get()
		if user :
				error = "This username is already taken"
		user = usersdb.Users.all().filter("email =" , email).get()
		if user:
				error = error +" the email i already used"
		if error !=" " :
				self.render("signup_form.html" ,error = user, username = user, email = email)
		else:
				password = userfun.hashed(password)
				cookie = username + "|" +userfun.cookistr(username)
				self.response.headers.add_header('Set-Cookie','user=%s'%str(cookie))

				user1 =usersdb.Users(username = username, password =password,email = email)
				user1.put()
				self.redirect("/")
class Login(Handler.Handler):
	def get(self):
		self.render("signup_form.html")
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		
		user = usersdb.Users.all().filter("username =",username).get()
		if user:
			passwordo = user.password
			salt = passwordo.split('|')[1]
			genpass = userfun.hashed(password , salt)
			if genpass == passwordo:
				cookie= username +"|"+userfun.cookistr(username)
				self.response.headers.add_header('Set-Cookie','user=%s'%str(cookie))
				self.redirect('/')
			else :
				self.render("signup_form.html", error="password or username ain't correct")
		else :
			self.render("signup_form.html", error="password or username ain't correct")


class Logout(Handler.Handler):
	def get(self):
		self.response.headers.add_header('Set-cookie','user=;')
		self.redirect('/')		

		

