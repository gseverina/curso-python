#!/usr/bin/python
import sys

def pepe():
	print 'Hello there', sys.argv[1]
	print sys.argv[0]

print __name__
if __name__ == '__main__':
	pepe()
