import constants
import Queue

class IO(object):

	def __init__(self, InputHandlerObject, OutputHandlerObject):
		# IS IT NEEDED?!!
		# InputHandlerObject.addQueue()
		self.__input = InputHandlerObject
		self.__inputState = self.__input.getState()
		self.inputQueue = self.__input.addQueue()

		self.__output = OutputHandlerObject
		self.__outState = self.__output.getState()

		self.__input.start()

	# Args to allow flexibility. Example: store meta information for Braille output
	# Also, the rectangle information for LCD
	def outputAll(self, buf, **args):
		for ID in self.__output.getAvailable():
			self.outputID(ID, buf, **args)

	def outputID(self, ID, buf, **args):
		self.__output.inout(ID, buf, **args)

	# For peripherals which support async input. All others must return None
	def asyncInput(ID, **args):
		return self.__input.inout(ID, -1, **args)

	# Array containing constants corresponding to connected peripherals
	def getAvailableInputs(self):
		return self.__input.getAvailable()

	# Array containing constants corresponding to connected output peripherals
	def getAvailableOutputs(self):
		return self.__output.getAvailable()

	def __delete__(self):
		self.__input.removeQueue(self.inputQueue)

	# In case we want to provide raw access to some output peripheral
	def getRawAccessOutputDevice(self, idx):
		pass