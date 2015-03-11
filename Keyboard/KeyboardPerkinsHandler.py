import DeviceHandler
import serial
from constants import *
from copy import deepcopy
from getch import *
import brailleParser
import time

class KeyboardPerkinsHandler(DeviceHandler.DeviceHandler):
	def __init__(self, inQ):
		DeviceHandler.DeviceHandler.__init__(self,inQ)
		self.disconnect()
		self.id = KEYBOARD_QWERTY
		self.char_list, self.rev_char_list = brailleParser.readFile('qwertyKeymap.txt')
		self.__delay__ = 0.10

	def disconnect(self):
		self.__available = None
		self.__input = None
		self.inQ.put({'sourceID' : self.id, 'signal': DEV_OFF})

	# Maintain kbd counter
	def initConnect(self):
		self.__available = True
		self.inQ.put({'sourceID' : self.id, 'signal': DEV_CONNECT})

	def readInput(self):
		#
		return None

	def run(self):
		while True:
			currentInput = self.readInput()
			if currentInput is None:
				if self.__available is None:
					pass
				else:
					self.disconnect()
				continue
			else:
			 	if self.__available is None:
			 		self.initConnect()
			 	self.__input = currentInput
			 	self.inQ.put({'sourceID' : self.id, 'input' : self.__input})