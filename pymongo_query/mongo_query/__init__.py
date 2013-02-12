import re


class PyMongoQuery(dict):

	def __and__(self, other):
		return PyMongoQuery(list(self.items()) + list(other.items()))

	def __or__(self, other):
		return PyMongoQuery({'$or': [self, other]})


class k(object):
	def __init__(self, key):
		self.key = key

	def __eq__(self, value):
		return PyMongoQuery({self.key: value})

	def __neq__(self, value):
		return PyMongoQuery({self.key: {'$ne': value}})

	def __gt__(self, value):
		return PyMongoQuery({self.key: {'$gt': value}})

	def __gte__(self, value):
		return PyMongoQuery({self.key: {'$gte': value}})

	def __lt__(self, value):
		return PyMongoQuery({self.key: {'$lt': value}})

	def __lte__(self, value):
		return PyMongoQuery({self.key: {'$lte': value}})

	def starts_with(self, string):
		return PyMongoQuery({self.key: {'$regex': '^' + re.escape(string)}})

	def ends_with(self, string):
		return PyMongoQuery({self.key: {'$regex': re.escape(string) + '$'}})