""" 
	Clone of $ cat /dev/random generating its own entropy.
	Nasko Apostolov
	9-29-2019
"""

import os
import sys
import random
import binascii
import struct

"""
    Default size of the kernel entropy pool.
"""
DEFAULT_ENTROPY = 4096

def dev_urandom_entropy(numbytes):
    """ 
        Reads random bytes from the /dev/urandom entropy pool.
		Previously released entropy is used if pool runs out.
    """	
    return os.urandom(numbytes)

def dev_random_entropy(numbytes, fallback_to_urandom=True):
    """ 
        Reads random bytes from the /dev/random pool.
		Blocks until more noise is generated in case the entropy pool runs out.
        Falls back to /dev/urandom on operating systems without /dev/random.
    """
    if os.name == 'nt' and fallback_to_urandom:
        return dev_urandom_entropy(numbytes)
    return open("/dev/random", "rb").read(numbytes)

"""
	Converts bytes to int.
"""        	
result = int.from_bytes(dev_random_entropy(DEFAULT_ENTROPY),byteorder=sys.byteorder) 	
print(result)