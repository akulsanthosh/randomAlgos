import threading

class Worker(threading.Thread):
	def __init__(self,c):
		super(Worker, self).__init__()
		self.c = c

	def run(self):
		while(True):
			print(self.c)


def main():
	c = input("Enter a no")
	thread = Worker(c)
	thread.start()



main()