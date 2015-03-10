import IOHandler
import Queue
from copy import deepcopy

import KeyboardHandler
##import QwertyKeyboardHandler
import GPIOHandler

## Concern: Should PERKIN and QWERTY be visible as different inputs to app? Or just have two keyboard interfaces?


class InputHandler(IOHandler.IOHandler):

	def __init__(self):
		IOHandler.IOHandler.__init__(self)
		self.inQ = Queue.Queue()
		self.__all =  {	KEYBOARD_UNO : KeyboardHandler(self.inQ), 
						# A class variable in KeyboardHandler stores the number of keyboards connected
						KEYBOARD_DOS : KeyboardHandler(self.inQ), 
						##KEYBOARD_QWERTY : QwertyKeyboardHandler(),
						GPIO_IN : GPIOHandler(self.inQ),
					}
		# List of all threads that want to listen to input changes. Synchronized queue maintained for each thread.
		# This thread puts into queue, the listener thread listens for it.
		self.active_listeners = []
		# input_source_id -> INT, input -> list of input
		self.__state = {}

	def addQueue(self):
		self.active_listeners.append(Queue.Queue())
		return self.active_listeners[-1]

	# Check if usage of remove is correct.
	def removeQueue(self, threadQueue):
		self.active_listeners.remove(threadQueue)


	# Main loop of the thread.
	def detectInputChange(self):
		# Device Handlers must return None if device not connected
		while True:
			# This must be a dictionary
			newInput = self.inQ.get()
			if 'signal' in newInput.keys():
				if newInput['signal'] == DEV_OFF:
					if newInput['sourceID'] in self.__available:
						self.__available.remove(newInput['sourceID'])
				elif newInput['signal'] == DEV_CONNECT:
					self.__available.add(newInput['sourceID'])
				continue
			for q in self.active_listeners:
				q.put(deepcopy(newInput))

		# Still need to call self.getAvailable periodically 

		# for idx in xrange(len(self._all)):
		# 	if 
		# 	new = currentInput[idx]
		# 	old = self.__state[idx]
		# 	# Each Device Handler must have a function ifStateEqual.
		# 	if not self.__all[idx].ifStateEqual(old, new):
		# 		ifChanged = True
		# 		self.setState(idx, new)
		# if ifChanged:
		# 	for q in self.active_listeners:
		# 		q.put(deepcopy(self.__state))
		# self.getAvailable()
