import DeviceHandler
import serial
from constants import *
from copy import deepcopy

class GPIOHandler(DeviceHandler.DeviceHandler):

	def __init__(self, inQ):
		DeviceHandler.DeviceHandler.__init__(self, inQ)
		self.disconnect()
		self.id = GPIO_IN


	def disconnect(self):
		self.__available = None
		self.__input = None
		self.inQ.put({'sourceID' : self.id, 'signal' : DEV_OFF})


	def initConnect(self):
		# For keyboard, also increase the Keyboard counter and so on
		self.__available = True
		self.inQ.put({'sourceID' : self.id, 'signal' : DEV_CONNECT})

	def readInput(self):
		# Do some bakchodi with serial library. Basically chepo older code
		# Return None if not able to talk
		return None

	# Main loop of thread
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
