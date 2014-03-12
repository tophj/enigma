# Rotor class for the engima

# Each rotor has a turnoverKey, which if hit, will cause the rotation of the next rotor in line.
# If the turnoverKey of the last rotor is hit, nothing will happen.

# Each rotor also contains a startingChar, which can be changed.






class Rotor:




	# Initializes a rotor with a default turnoverKey and startingChar
	def __init__(self):

		self.turnoverKey = "R"
		self.startingChar = "A"

		self.nextRotor = None
	

	# Wrapper for changing the starting character
	def changeStartingChar(self, char):

		if char.isalpha():
			self.startingChar = char.upper()

		else:
			print "Character entered is invalid, can't change starting character"

	def changeTurnoverKey(self, key):

		if key.isalpha():
			self.turnoverKey = key.upper()

		else:
			print "Character entered is invalid, can't change turnover key"

	def setNextRotor(self, rotor):

		if isinstance(rotor,Rotor):
			self.nextRotor = rotor
			
		else:
			print "Invalid rotor."



	def encrypt(self, char):





# a = Rotor()
# b = Rotor()


# a.setNextRotor(b)