#!/usr/bin/env python2.7


class Format(object):
	data = None
	def __init__(self, name, test):
		print 'Initializing format: %s' % name
		self.test = test
	def __call__(self, data):
		if self.test(data):
			return data
		else:
			return False

ANY       = 0
STRING    = 1
NUMBER    = 2
FILE_PATH = 3

string = Format(
	name='String',
	test=lambda data: type(data) == str
)

def test(data):
	try:
		float(data)
		return True
	except:
		return False
number = Format(
	name='Number',
	test=test
)


def test(data):
	try:
		float(data)
		return True
	except:
		return False
file_path = Format(
	name='File',
	test=test
)


