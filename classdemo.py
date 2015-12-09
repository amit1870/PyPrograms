class Person(object):
	def __init__(self,name,gender,age):
		self.name = name
		self.gender = gender
		self.age = age

	def printQuality(self):
		print self.name,self.gender,self.age


class Job(object):
	def __init__(self,type):
		self.type = type

	def printQuality(self):
		print self.type


class Employee(Person,Job):
	def __init__(self,name,gender,age,type):

		super(Employee,self).__init__(name,gender,age)
		# super(Employee,self).__init__(type)
	

emp = Employee("Amit","Male",27,"Engineer")

