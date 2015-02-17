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
print "------------------ Enigma Encrpyt / Decrpyt ------------------"
print "To start, type plaintext and it will be encrypted."
print "Or, type in ciphertext and it will be decrypted."
print ""
print "Rotors are reset in between encryptions."
print "To exit, type '!'"
print "--------------------------------------------------------------"
print ""


class Enigma:

	def __init__(self):

		# Set up 
		self.firstRotor = Rotor(1)
		self.secondRotor = Rotor(2)
		self.thirdRotor = Rotor(3)
		self.theReflector = Reflector('B')
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


	def readInput(self):

		# Start reading 
		line = sys.stdin.readline()

		while(line != "!\n"):
			wordToEncrypt = line.rstrip()
			originalWord = wordToEncrypt		
			wordToEncrypt = wordToEncrypt.replace(" ","")

			if wordToEncrypt is not None and wordToEncrypt.isalpha():
				encryptedLength = len(wordToEncrypt)
				encryptedWord = ""
				print "--------------------------------------------------------------"
				print(" In Plugboard R1  R2  R3  Reflector R3  R2  R1  Plugboard Out ")
				for i in range(0,encryptedLength):
				

					char = wordToEncrypt[i].upper()
					sys.stdout.write(" " + char + "   ")
					
					char = self.thePlugboard.changeString(char)
					sys.stdout.write(char + "         ")
					
					firstOutput = self.firstRotor.encrypt(char)
					sys.stdout.write(firstOutput + "   ")
					secondOutput = self.secondRotor.encrypt(firstOutput)
					sys.stdout.write(secondOutput + "   ")
					thirdOutput = self.thirdRotor.encrypt(secondOutput)
					sys.stdout.write(thirdOutput + "   ")

					outputReflector = self.theReflector.getMapping(thirdOutput)
					sys.stdout.write(outputReflector + "         ")

					thirdOutput = self.thirdRotor.postEncrypt(outputReflector)
					sys.stdout.write(thirdOutput + "   ")
					secondOutput = self.secondRotor.postEncrypt(thirdOutput)
					sys.stdout.write(secondOutput + "   ")
					firstOutput = self.firstRotor.postEncrypt(secondOutput)
					sys.stdout.write(firstOutput + "   ")
					plugboardOutput = self.thePlugboard.changeString(firstOutput)
					sys.stdout.write(plugboardOutput + "         " + plugboardOutput + "  \n")
					self.firstRotor.increment()

					encryptedWord += plugboardOutput
				print "--------------------------------------------------------------"
				print ""
				print originalWord, " encrypted as: ", encryptedWord
				print ""
				
				self.firstRotor.reset()
				self.secondRotor.reset()
				self.thirdRotor.reset()

			else:
				print "Error: Word can only contain letters in the alphabet.\n"

			line = sys.stdin.readline()


if __name__ == "__main__":

	runEnigma = Enigma()
	runEnigma.readInput()






