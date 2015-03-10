import threading

from constants import *

class IOHandler(threading.Thread)

	def __init__(self):
		# Mapping from name to objects
		threading.Thread.__init__(self)
		# Defined in subclass InputHandler and OutputHandler
		self.__all =  {}
		self.__available = getAvailable()
		# Defined in subclass. Array of size _all. None if device not connected.
		self.__state = [None for each in self.__all]


	def getAvailable(self):
		# Each object of the Handler Class spawns a course granularity thread for monitoring changes in availability 
		self.__available = {inp:self.__all[inp] for inp in self.all.keys() if self.__all[inp].available is not None}
		return self.available.keys()

	def inout(self, ID, buf, **args):
		try:
			_dev = self.__available[ID]
			# Inout is an async function. Input and output not separated to keep the logic of InputHandler and Output Handler same
			# Also handle device disconnect in _dev.inout
			return _dev.inout(buf,**args) 
		except KeyError:
			pass


	# Check if garbage collector messes when states are objects
	def setState(self, idx, value):
		self.__state[idx] = value

