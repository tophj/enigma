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
		self.previousRotor = None
	

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


	def setPreviousRotor(self, rotor):

		if isinstance(rotor,Rotor):
			self.previousRotor = rotor

		else:
			print "Invalid rotor."




	# The rotors should already be incremented properly. Only takes a letter and figures out what it should be using
	# a substitution cipher based off the starting key
	def encrypt(self, char):

		# It's the last rotor; send it to the reflector
		# if self.nextRotor is None:
		# 	#We know we are looking at the reflector

		# else:
		# determines key offset, which is starting key ascii value - ascii value of "A"
		keyOffset = ord(self.getStartingKey()) - 65

		asciiChar = ord(char.upper())
		newAsciiChar = (asciiChar + keyOffset)

		if newAsciiChar > 90: 
			newOffset = newAsciiChar - 90
			newAsciiChar = 64 + newOffset


		encryptedChar = chr(newAsciiChar)
		
		return encryptedChar


	# Post encrypt is used to encrypt a character after sending it through all three rotors
	# and back through the reflector	
	def postEncrypt(self,char):

		keyOffset = abs(ord(self.getStartingKey()) - ord(char))
		asciiValue = keyOffset + 65

		postEncryptChar = chr(asciiValue)



		# This means it is the first rotor, so send it to the lightbulbs aka print it
		if self.previousRotor is None:
			#print "Final encrypted character is : ", postEncryptChar
			return postEncryptChar
		else:

			return postEncryptChar


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