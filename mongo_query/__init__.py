import re


class mongo_query(dict):

	def __and__(self, other):
		return mongo_query(list(self.items()) + list(other.items()))

	def __or__(self, other):
		return mongo_query({'$or': [self, other]})


class k(object):
	def __init__(self, key):
		self.key = key

	def __eq__(self, value):
		return mongo_query({self.key: value})

	def __neq__(self, value):
		return mongo_query({self.key: {'$ne': value}})

	def __gt__(self, value):
		return mongo_query({self.key: {'$gt': value}})

	def __gte__(self, value):
		return mongo_query({self.key: {'$gte': value}})

	def __lt__(self, value):
		return mongo_query({self.key: {'$lt': value}})

	def __lte__(self, value):
		return mongo_query({self.key: {'$lte': value}})

	def starts_with(self, string):
		return mongo_query({self.key: {'$regex': '^' + re.escape(string)}})
	
	def ends_with(self, string):
		return mongo_query({self.key: {'$regex': re.escape(string) + '$'}})