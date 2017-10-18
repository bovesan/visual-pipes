#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import visualpipes.formats
import visualpipes.blocks


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_formats(self):
    	self.assertEqual('hello world', visualpipes.formats.string('hello world'))
    	self.assertFalse(visualpipes.formats.string(42))
    	self.assertEqual('42', visualpipes.formats.number('42'))
    	self.assertEqual('1234567.8', visualpipes.formats.number('1234567.8'))
    	self.assertEqual('-1234567.8', visualpipes.formats.number('-1234567.8'))
    	self.assertFalse(visualpipes.formats.number('text'))

    def test_blocks(self):
    	visualpipes.blocks.read.Create()


if __name__ == '__main__':
	unittest.main()
