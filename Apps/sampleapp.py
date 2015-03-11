import threading
from constants import *
from time import time
from englishBrl import *
class MenuApp(threading.Thread):

	MENU_TIMEOUT = 10

	def __init__(self, IOObject):
		threading.Thread.__init__(self)
		self.IO = IOObject
		# self.displayState = {}


	def displayMenu(self, arg):
		print arg
		# Outputs menu on all output peripherals based on displayState
		# self.IO.outputID(LCD_DISPLAY, "Welcome User!", topLeft={0,0}, bottomRight={64,10})
		# self.IO.outputID(SPEAKER_AUDIO, "audio/menu/welcome.mp3", audioType=AUDIO_MP3)
		# self.IO.outputID(RBC_OUT, self.displayState['brailleOut'], display=RBC_MANUAL_SCROLL)
		# Lots of stuff here
		pass

	def updateDisplayState(self, input):
		if input['sourceID'] == KEYBOARD_QWERTY:
			return fromBraille([convertToBinary(input['input'])])
		else:
			return 'Bhasad'

	# Main loop
	def run(self):
		self.displayMenu('Welcome Buddy!')
		# currentTime = time()
		while True:
			# If no input for long time, repeat
			# if time() - currentTime > MENU_TIMEOUT:
			# 	self.displayMenu()
			# 	currentTime = time()
			# This usage of Queue.get() is most probably inconsistent with the timeout shown above. Correct this.
			newInput = self.IO.inputQueue.get()
			# print 'Got input...'
			# if new input recorded
			if newInput:
				ret = self.updateDisplayState(newInput)
				self.displayMenu(ret)
