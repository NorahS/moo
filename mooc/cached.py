from google.appengine.api import memcache


def cached(name):
	return memcache.get(name)== None
def cache (name,p):
	memcache.set(name, p)


