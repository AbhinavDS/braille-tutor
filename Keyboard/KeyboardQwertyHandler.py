import DeviceHandler
import serial
from constants import *
from copy import deepcopy
from getch import *
import time
import Queue
from qwerty import *
import thread

class KeyboardQwertyHandler(DeviceHandler.DeviceHandler):
	def __init__(self, inQ):
		DeviceHandler.DeviceHandler.__init__(self,inQ)
		self.id = KEYBOARD_QWERTY
		self.disconnect()
		self.__delay__ = 0.10
		self.perQ = Queue.Queue()
		try:
			thread.start_new_thread(readQwerty, (self.perQ, ))
		except:
			print 'Couldn\'t start kb thread'
	def disconnect(self):
		self.__available = None
		self.__input = None
		self.inQ.put({'sourceID' : self.id, 'signal': DEV_OFF})

	def initConnect(self):
		self.__available = True
		self.inQ.put({'sourceID' : self.id, 'signal': DEV_CONNECT})

	# Issues: When to send None 
	def readInput(self):
		a = self.perQ.get()
		time.sleep(self.__delay__)
		while not self.perQ.empty():
			a += self.perQ.get()
		return a

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
