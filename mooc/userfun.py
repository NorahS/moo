import random, string , hashlib

def saltmkr():
	return"".join(random.choice(string.letters ) for i in range(5))

def hashed (pas, salt= ''):
	if salt == '':
		salt = saltmkr()
	hashed = hashlib.sha256(pas+salt).hexdigest()
	hashed = hashed + '|'+salt
	return hashed

def cookistr( username):
	return hashlib.sha256( username + "cool" +username).hexdigest()

