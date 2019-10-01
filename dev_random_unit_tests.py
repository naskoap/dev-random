""" 
	Unit tests for /dev/random entropy generator.
	Nasko Apostolov
	9-29-2019
"""

import unittest

import os
import sys
import string
import binascii

from dev_random_main.dev_random import dev_random_entropy, dev_urandom_entropy, DEFAULT_ENTROPY

class EntropyTests(unittest.TestCase):
    def test_dev_urandom_entropy(self):
        bytes16 = dev_urandom_entropy(DEFAULT_ENTROPY)
        self.assertEqual(len(bytes16), DEFAULT_ENTROPY)

    def test_dev_random_entropy(self):
        bytes16 = dev_random_entropy(DEFAULT_ENTROPY)
        self.assertEqual(len(bytes16), DEFAULT_ENTROPY)

    def test_dev_random_entropy_fallback(self):
        os.name = 'nt'
        bytes16 = dev_random_entropy(DEFAULT_ENTROPY)
        self.assertEqual(len(bytes16), DEFAULT_ENTROPY)

if __name__ == '__main__':
    unittest.main()