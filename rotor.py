# Rotor class for the engima

# Each rotor has a turnoverKey, which if hit, will cause the rotation of the next rotor in line.
# If the turnoverKey of the last rotor is hit, nothing will happen.

# Each rotor also contains a startingChar, which can be changed.


class Rotor:

	# Initializes a rotor with a default turnoverKey, startingKey, and mapping

	def __init__(self, version=None):
		# Royal Flags Wave Kings Above, starting keys RFWKA for rotors 1-5
		if(version is 1):
			self.turnoverKey = "R"
			self.currentKey = "E"
			self.startingKey = "E"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']

		elif(version is 2):
			self.turnoverKey = "F"
			self.currentKey = "A"
			self.startingKey = "A"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']

		elif(version is 3):
			self.turnoverKey = "W"
			self.currentKey = "B"
			self.startingKey = "B"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']

		elif(version is 4):
			self.turnoverKey = "K"
			self.currentKey = "E"
			self.startingKey = "E"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']

		elif(version is 5):
			self.turnoverKey = "A"
			self.currentKey = "V"
			self.startingKey = "V"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']
		# set it equal to the testing rotor
		else:
			self.turnoverKey = "E"
			self.currentKey = "A"
			self.startingKey = "A"
			self.nextRotor = None
			self.previousRotor = None
			self.alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
		self.currentIndex = 0;

	# wrapper for getting the current key
	def getCurrentKey(self):
		return self.currentKey

	# wrapper for getting the starting key
	def getStartingKey(self):
		return self.startingKey

	# Wrapper for changing the starting key
	def changeStartingKey(self, char):
		if char.isalpha():
			self.currentKey = char.upper()
			self.startingKey = char.upper()

			for char2 in self.alphabet:
				if(char2 == char):
					break
				self.currentIndex += 1
		else:
			print "Character entered is invalid, can't change starting character"

	# wrapper for getting the turnover key: the key which causes the next rotor to increment
	def getTurnoverKey(self):
		return self.turnoverKey

	# wrapper for changing the turnover key: the key which causes the next rotor to increment
	def changeTurnoverKey(self, key):
		if key.isalpha():
			self.turnoverKey = key.upper()
		else:
			print "Character entered is invalid, can't change turnover key"

	# sets the nextRotor attribute for the current rotor
	def setNextRotor(self, rotor):
		if isinstance(rotor,Rotor):
			self.nextRotor = rotor	
		else:
			print "Invalid rotor."

	# set the previousRotor attribute for the current rotor
	def setPreviousRotor(self, rotor):
		if isinstance(rotor,Rotor):
			self.previousRotor = rotor
		else:
			print "Invalid rotor."

	# returns the nextRotor attribute for the current rotor if not None
	def getNextRotor(self):
		if self.nextRotor is not None:
			return self.nextRotor
		else:
			print "Next Rotor is None."

	# returns the previousRotor attribute for the current rotor if not None
	def getPreviousRotor(self):
		if self.previousRotor is not None:
			return self.previousRotor			
		else:
			print "Previous Rotor is None."

	# Takes a char and encrypts it using a substitution cipher based off an incrementing offset
	def encrypt(self, char):
		asciiCharInt = ord(char.upper())
		newAsciiCharIndex = ((asciiCharInt - 65) + self.currentIndex) % 26
		encryptedChar = self.alphabet[newAsciiCharIndex]

		return encryptedChar

	# Inverse of encrypt(); used after the char returns from the reflector. 
	# Takes a char and encrypts it using a substitution cipher based off an incrementing offset
	def postEncrypt(self,char):
		indexOfInputChar = 0
		for char2 in self.alphabet:
			if(char2 == char):
				break
			indexOfInputChar += 1

		shiftedIndex = (indexOfInputChar - self.currentIndex) % 26
		asciiValue = shiftedIndex + 65
		postEncryptChar = chr(asciiValue)
		
		return postEncryptChar

	# Increments the a rotor by one until it reaches the turnover key, then it increments the next rotor if it's not the last rotor 
	def increment(self):
		if self.currentKey == self.turnoverKey:
			if self.nextRotor is not None:
				self.nextRotor.increment()
		elif self.nextRotor is not None:
			if self.nextRotor.currentKey == self.nextRotor.turnoverKey:
				self.nextRotor.increment()

		self.currentIndex = (self.currentIndex + 1) % 26
		self.currentKey = self.alphabet[self.currentIndex]

	# Resets the rotor to it's initial settings defined by changeTurnoverKey and changeStartingKey or the defaults
	def reset(self):
		self.changeStartingKey(self.startingKey)
		self.currentIndex = 0;






