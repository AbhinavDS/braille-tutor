from constants import *
import threading

class DeviceHandler(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		# Define in subclass
		self.__input = None
		# Must be None only if corresponding device not connected 
		self.available = False

	# Define all of the following functions in subclass. For example, a keyboard input will only be unequal if a state is different from the last valid state.
	# i.e., the state when the input is all zero doesn't count.
	def ifStateEqual(self, a, b):
		pass
		return False

	def getInput(self):
		pass
		return None

	# Used for writes and async reads. Not None only if an async device.
	def inout(self, buf, **args):
		pass
		return None

	# Main thread of the loop. Should at least update self.__input, self.__available.
	# Also handles reconnects, connects and disconnects.
	def run(self):
		pass