# Mongo Query


A lightweight library that overloads several operators to make writing PyMongo-compatible MongoDB queries a lot nicer.

## Usage
	
	>>> User.find((k('username') == 'fletom') | (k('name').starts_with('Fletcher')))
	...
	>>> User.find(k('reputation') > 10)
	...

Instead of:

	>>> User.find({'$or': [{'username': 'fletom'}, {'name': {'$regex': '^Fletcher'}}]})
	...
	>>> User.find({'reputation': {'$gt': 10}})
	...

## Documentation

There's not much to it. The `k` objects support all of Python's comparison operators, in addition to `.starts_with(s)` and `.ends_with(s)`. `PyMongoQuery` is a `dict` subclass that supports logical `and` and `or` using the `&` and `|` syntax. If you think a feature should be added, feel free to send in a pull request.