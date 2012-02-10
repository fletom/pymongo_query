Mongo Query
============

A lightweight library that overloads several operators to make writing PyMongo-compatible MongoDB queries a lot nicer.

Usage:

	>>> from mongo_query import k
	>>> k('username') == 'nomulous'
	{'username': 'nomulous'}
	>>> (k('username') == 'nomulous') & (k('reputation') > 10)
	{'username': 'nomulous', 'reputation': {'$gt': 10}}