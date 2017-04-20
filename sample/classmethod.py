# a simple demo for checking the working of different class functions

class Display:
	
	#  holds the reference to the newly created instance
	def __init__(self):
		print 'yo in the Display cons'
		self.ram = self.ram('abhishek', 'goswami')
		self.display = self.display()
	
	def display(self):
		print 'in the simple display function'

	@classmethod
	# cls is an object that holds the class itself
	def ram(cls, fname, lname):
		print 'in the overloaded cons'
		print 'you name is ' + fname + ' ' + lname

	@classmethod
	def ganshyam(cls, fname, lname):
		print 'yo gaanshyam'

	# does not require instance
	@staticmethod
	def shyam(fname, lname):
		print fname + ' ' + lname

#obj = Display.ram('abhishek', 'goswami');
#obj = Display.shyam('hiro', 'dev');

obj = Display()
