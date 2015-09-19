from datetime import datetime

intit = lambda x : int(x)

class Life(object):
	def __init__(self,janama,dob):
		self.janama = janama
		self.dob = self.makeDOB(dob)
		self.gf = 0


	def makeDOB(self,dob):
		dob = dob.split("-")
		dob = map(intit, dob)
		dob = {'yyyy':dob[2], 'mm':dob[1], 'dd':dob[0]}
		dob = datetime(dob['yyyy'],dob['mm'],dob['dd'])
		return dob

	def gfEntry(self):
		self.gf += 1

	def hasFallenInLove(self):
		return self.gf > 0 


	def hasGirlFriends(self):
		return self.gf > 0 


	def isEnjoying(self):
		return self.hasGirlFriends()



	def isAlive(self):
		self.now = datetime.now()
		self.diff = self.now - self.dob
		if self.diff.days >= 36500:
			return False
		return True





life = Life("Manusya","12-06-1989")


if __name__ == "__main__":
	if life.isAlive():
		life.gfEntry()
		if life.isEnjoying():
			print "He"

		pass
	else:
		print "It is Dead."
