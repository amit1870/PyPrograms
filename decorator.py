def helloSolar(orgi_func):
	def new_func(*args, **kwargs):
		orgi_func(*args, **kwargs)
		print "Hello Solar"
	return new_func

def helloGalaxy(orgi_func):
	def new_func(*args, **kwargs):
		orgi_func(*args, **kwargs)
		print "Hello Galaxy"
	return new_func

@helloGalaxy
@helloSolar
def hello(target=None):
	if target:
		print "Hello " + target
	else:
		print "Hello World"

hello("Earth")