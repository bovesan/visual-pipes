#!/usr/bin/env python2.7

print 'block module loaded'

class Block(object):
	def __init__(self, name, connectors_input, connectors_output, connectors_output_failed):
		self.name = name
		self.connectors_input = connectors_input
		self.connectors_output = connectors_output
		self.connectors_output_failed = connectors_output_failed
		print 'New block initialized: %s' % self.name

