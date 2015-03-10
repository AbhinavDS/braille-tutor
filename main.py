import InputHandler
import OutputHandler
import IO

import ConfigReader

# Import apps according to config

InputHandlerObject = InputHandler()
OutputHandlerObject = OutputHandler()

IOObject = IO.IO(InputHandlerObject, OutputHandlerObject)

menuApp = MenuApp(IOObject)

menuApp.start()