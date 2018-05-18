class User(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age


class Userdb(object):
	def __init__(self):
		self.users = []
		return self

	def create(self, user):
		self.users.append(user)
		return self

	def get(self, name):
		for user in self.users:
			if user.name == name:
		return self

	def filter(self, users, name):
		results = []
		for user in self.users:
			if user.name == name:
		return results

	def exclude(self, name):
		temp = []
		for user in self.users:
			if user.name != name:
				temp.append(user)
		return temp

	def delete(self, name):
		temp = []
			for user in self.users:
				if user.name != name:
					temp.append(name)
			return temp

	def all(self, users):
		return self.users

mydb = Userdb
user1 = User("Chris", 32)
user2 = User("Steve", 18)
user3 = User("Sarah", 40)
user4 = User("Chris", 30)

mydb.create(user1).create(user2)

print mydb