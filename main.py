import sys
import os
sys.path.append(os.getcwd() + '/Apps/')
sys.path.append(os.getcwd() + '/Parser/')
sys.path.append(os.getcwd() + '/Keyboard/')
sys.path.append(os.getcwd() + '/GPIO/')

import InputHandler
import OutputHandler
import IO
from sampleapp import *

# import ConfigReader

# Import apps according to config

InputHandlerObject = InputHandler.InputHandler()
OutputHandlerObject = OutputHandler.OutputHandler()

IOObject = IO.IO(InputHandlerObject, OutputHandlerObject)

menuApp = MenuApp(IOObject)

menuApp.start()

while 1:
	pass