import thread
import os
from getch import *
import brailleParser

char_list, rev_char_list = brailleParser.readFile(os.getcwd() + '/Keyboard/qwertyKeymap.txt')
def readQwerty(perQ):
	while 1:
		a = getch().lower()
		if a==' ': #space
			a = '\s'
		if a=='\x7f': #backspace
			a = "\\x7f"
		elif a=='\r': #enter
			a = "\\r"
		if not a in char_list:
			continue 
		perQ.put(char_list[a])



