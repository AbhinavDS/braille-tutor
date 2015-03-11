import IOHandler 
from constants import *

# import RBCHandler
# import SpeakerHandler
# import LCDHandler

class OutputHandler(IOHandler.IOHandler):

	def __init__(self):
		IOHandler.IOHandler.__init__(self)
		self.__all =  {	}
						# LCD_DISPLAY : LCDHandler(), 
						# RBC_OUT : RBCHandler(), 
						# SPEAKER_AUDIO : SpeakerHandler(),
					# }


	# Main loop of thread
	def run(self):
		while True:
			self.getAvailable()