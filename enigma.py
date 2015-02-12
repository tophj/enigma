# -----------------------------------------------------------------------------------
#  _______________________________ 
# < Enigma - by Christopher Jones >
#  ------------------------------- 
# 
# The Enigma consists of 5 stages. 
# 1. The Keyboard: This implementation uses a standard 26-character alphabet
# 2. The Plugboard: Contains up to 13 mappings for characters output from the keyboard
# 3. The Rotors (part I) : Contains 3 rotors that individually offer a shift cipher, but move after every key press
#        resulting in a polyalphabetic cipher
# 4. The Reflector : Contains 13 character mappings to ensure the same character is not encoded to itself
# 5. The Rotors (part II) : Going in reverse order from part I, this time the rotors do not increment, used so
#        that the Enigma can be used to both encrypt and decrypt a message
# -----------------------------------------------------------------------------------

from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

import sys


print ""
print "---------------- Welcome to Enigma ----------------"
print "To start, type a word and it will be encrypted."
print "To exit, type '!'"
print "---------------------------------------------------"
print ""


class Enigma:

	def __init__(self):

		# Set up 
		self.firstRotor = Rotor()
		self.secondRotor = Rotor()
		self.thirdRotor = Rotor()
		self.theReflector = Reflector()
		self.thePlugboard = Plugboard()

		# Set the order of the rotors
		self.firstRotor.setNextRotor(self.secondRotor)
		self.secondRotor.setNextRotor(self.thirdRotor)
		self.thirdRotor.setPreviousRotor(self.secondRotor)
		self.secondRotor.setPreviousRotor(self.firstRotor)

		# Set the keys which turnover the next rotor
		self.firstRotor.changeTurnoverKey("R")
		self.secondRotor.changeTurnoverKey("F")
		self.thirdRotor.changeTurnoverKey("W")

		# Set the starting key for the rotor
		self.firstRotor.changeStartingKey("G")
		self.secondRotor.changeStartingKey("K")
		self.thirdRotor.changeStartingKey("O")

	def readInput(self):

		# Start reading 
		line = sys.stdin.readline()

		while(line != "!\n"):
			wordToEncrypt = line.rstrip()
			originalWord = wordToEncrypt		
			wordToEncrypt = wordToEncrypt.replace(" ","")
			wordToEncrypt = self.thePlugboard.changeString(wordToEncrypt)

			if wordToEncrypt is not None and wordToEncrypt.isalpha():
				encryptedLength = len(wordToEncrypt)
				encryptedWord = ""

				for i in range(0,encryptedLength):
					char = wordToEncrypt[i]

					self.firstRotor.increment()
					firstOutput = self.firstRotor.encrypt(char)
					secondOutput = self.secondRotor.encrypt(firstOutput)
					thirdOutput = self.thirdRotor.encrypt(secondOutput)

					outputReflector = self.theReflector.getMapping(thirdOutput)

					thirdOutput = self.thirdRotor.postEncrypt(outputReflector)
					secondOutput = self.secondRotor.postEncrypt(thirdOutput)
					firstOutput = self.firstRotor.postEncrypt(secondOutput)

					encryptedWord += firstOutput

				print ""
				print originalWord, " encrypted as: ", encryptedWord
				print ""
				
				self.firstRotor.reset()
				self.secondRotor.reset()
				self.thirdRotor.reset()

			line = sys.stdin.readline()


if __name__ == "__main__":

	runEnigma = Enigma()
	runEnigma.readInput()






