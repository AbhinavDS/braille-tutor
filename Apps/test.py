
import Queue
import KeyboardQwertyHandler
import time
q = Queue.Queue()
kb = KeyboardQwertyHandler.KeyboardQwertyHandler(q)
kb.start()

while 1:
	while not q.empty():
		print q.get()
	print '**\n\n'
	time.sleep(2)
