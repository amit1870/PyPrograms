from datetime import datetime
from time import sleep


class Life(object):

	def __init__(self,janama,dob,gender):
		self.janama = janama
		self.gender = gender
		self.dob = self.makeDOB(dob)
		self.gf = 0
		self.study = {}
		self.satisfied = None
		self.spouse = None
		self.age = self.getAge()
		self.karma = {'Paropkar':0,'Apkar':0}
		self.tension = None
		self.loan = None

	def intList(self):
		return lambda x : int(x)

	def doStudy(self,course):
		self.study[course] = True

	def hasDegree(self):
		return self.study

	def hasJob(self):
		if self.study:
			if self.study.has_key('SSC'):
				if self.study.has_key('HSC'):
					if self.study.has_key('B.Tech'):
						return "Engineer"
					return "Operator"
				return "Peon"
		return "Laborour"

	def isLookingForSpouse(self):
		print "Checking whether This Prani is looking for spouse ?",
		sleep(1)
		print "..."
		sleep(1)
		if not self.spouse:
			if self.gender == 'Male':
				if self.getAge() >= 26:
					return True
				return False

			elif self.gender == 'Female':
				if self.study.has_key('B.Tech'):
					if self.getAge() >= 25:
						return True
					return False
				else:
					if self.getAge() >= 20:
						return True
					return False

			else:
				print "This Prani cannot get married."
				return False

		return False



	def getMarried(self,name):
		self.spouse = name
		self.gf += 1

	def isSatisfied(self):
		if self.spouse and self.hasJob() and self.isEnjoying():
			return True

		elif self.hasJob() and self.isEnjoying() and not self.spouse:
			print "This Prani has girl friends and enjoying right now. Not looking for spouse."
			return True

		elif self.hasJob() and not self.isEnjoying() and not self.spouse:
			print "This Prani has job but not enjoying and looking for spouse."
			return False

		elif not self.hasJob():
			print "This Prani is looking for job."
			return False


	def makeDOB(self,dob):
		dob = dob.split("-")
		dob = map(self.intList(), dob)
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

	def getAge(self):
		self.now = datetime.now()
		self.diff = self.now - self.dob
		return self.diff.days / 365

	def doingKarma(self,karma):
		self.karma[karma] += 1

	def hasTension(self):
		if not life.isEnjoying:
			return True
		return False

	def hasLoan(self):
		if self.hasJob() == 'Engineer':
			return True

		return False


	def isAlive(self):
		self.now = datetime.now()
		self.diff = self.now - self.dob
		if self.diff.days >= 36500:
			return False
		return True

	def afterDeath(self):
		if self.karma['Paropkar'] >= self.karma['Apkar']:
			return "This Prani goes to Swarg.."

		return "This Prani goes to Narka.."



life = Life("Prani","12-06-1989","Male")


if __name__ == "__main__":
	if life.isAlive():
		# life.gfEntry()
		life.doStudy("SSC")
		life.doStudy("HSC")
		life.doStudy("Preparation")
		life.doStudy("B.Tech")

		# print life.hasDegree()
		print life.hasJob()
		if life.isLookingForSpouse():
			life.getMarried("XYX")
		# print life.spouse
		# print life.isSatisfied()
		# print life.isLookingForSpouse()

		print life.isSatisfied()
		for x in range(0,1000):
			if x % 4 == 0:
				life.doingKarma('Apkar')
			else:
				life.doingKarma('Paropkar')

		# print life.karma
		# print life.hasFallenInLove()
		# print life.hasTension()
		# print life.hasLoan()
		if life.isEnjoying():
			print "This Prani is enjoying a lot.."

	else:

		print "It is Dead."
		print life.afterDeath()
