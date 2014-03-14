# Rotor class for the engima

# Each rotor has a turnoverKey, which if hit, will cause the rotation of the next rotor in line.
# If the turnoverKey of the last rotor is hit, nothing will happen.

# Each rotor also contains a startingChar, which can be changed.






class Rotor:




	# Initializes a rotor with a default turnoverKey and startingKey
	def __init__(self):

		self.turnoverKey = "R"
		self.startingKey = "A"

		self.nextRotor = None
	

	# Wrapper for changing the starting character
	def changeStartingKey(self, char):

		if char.isalpha():
			self.startingKey = char.upper()

		else:
			print "Character entered is invalid, can't change starting character"


	def getStartingKey(self):

		return self.startingKey

	def changeTurnoverKey(self, key):

		if key.isalpha():
			self.turnoverKey = key.upper()

		else:
			print "Character entered is invalid, can't change turnover key"


	def getTurnoverKey(self):

		return self.turnoverKey


	def setNextRotor(self, rotor):

		if isinstance(rotor,Rotor):
			self.nextRotor = rotor
			
		else:
			print "Invalid rotor."


	# The rotors should already be incremented properly. Only takes a letter and figures out what it should be using
	# a substitution cipher based off the starting key
	def encrypt(self, char):

		# It's the last rotor; send it to the reflector
		if self.nextRotor is None:
			print "Increment reflector"

		else:
			# determines key offset, which is starting key ascii value - ascii value of "A"
			keyOffset = ord(self.startingKey) - 65

			asciiChar = ord(char)
			newAsciiChar = asciiChar + keyOffset % 90

			if newAsciiChar < 65:
				newAsciiChar += 64

			encryptedChar = chr(newAsciiChar)
			
			return encryptedChar


		

	# Uppercase ASCII values are 65 - 90 (A-Z)
	def increment(self):



		asciiNewStartingChar = ord(self.startingKey) + 1

		if asciiNewStartingChar > 90:
			asciiNewStartingChar = 65

		self.changeStartingKey(chr(asciiNewStartingChar))

		if self.startingKey == self.turnoverKey:
			if self.nextRotor is not None:
				self.nextRotor.increment()



# a = Rotor()
# b = Rotor()


# a.setNextRotor(b)