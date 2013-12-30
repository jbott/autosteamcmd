import sys
import config

CSI     = '\033['
BLACK 	= 30
RED     = 31
GREEN   = 32
YELLOW  = 33
BLUE    = 34
MAGENTA = 35
CYAN    = 36
WHITE   = 37
RESET   = 39

GOOD	= GREEN
BAD	= RED
WARN	= YELLOW

def colorcode(code):
	return '{}{}{}'.format(CSI, code, 'm')

def printc(string, color=None):
	if config.COLOR and color != None:
		sys.stdout.write(colorcode(color))
	sys.stdout.write(string)
	if config.COLOR and color != None:
		sys.stdout.write(colorcode(RESET))

def printcln(string, color=None):
	printc(string, color)
	sys.stdout.write('\n')
