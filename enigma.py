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
import logging


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


	def readInput(self, argv):
		logger = logging.getLogger()
		logger.setLevel(logging.INFO)

		ch = logging.StreamHandler(sys.stdout)
		ch.setLevel(logging.DEBUG)

		logger.addHandler(ch)
		# Read in args, check to see if verbose statements (-v) are on 
		for arg in argv[1:]:
			if arg == '-v':
				logger.setLevel(logging.DEBUG)
			else:
				print "Invalid parameter " + arg + ". Correct useage is:\npython enigma.py \nOR\npython enigma.py -v \nfor step by step encryption/decryption results.\n"
				sys.exit(0)


		# Start reading 
		line = sys.stdin.readline()

		while(line != "!\n"):
			wordToEncrypt = line.rstrip()
			originalWord = wordToEncrypt		
			wordToEncrypt = wordToEncrypt.replace(" ","")

			if wordToEncrypt is not None and wordToEncrypt.isalpha():
				encryptedLength = len(wordToEncrypt)
				encryptedWord = ""
				logging.debug("--------------------------------------------------------------")
				logging.debug(" In Plugboard R1  R2  R3  Reflector R3  R2  R1  Plugboard Out")
				
				for i in range(0,encryptedLength):
					debugLine=  ""
					charUpper = wordToEncrypt[i].upper()
					
					# go through plugboard, rotors 1-3, reflector, rotors 3-1, plugboard and out
					char = self.thePlugboard.changeString(charUpper)
					firstOutput = self.firstRotor.encrypt(char)				
					secondOutput = self.secondRotor.encrypt(firstOutput)					
					thirdOutput = self.thirdRotor.encrypt(secondOutput)
					outputReflector = self.theReflector.getMapping(thirdOutput)
					thirdOutputRe = self.thirdRotor.postEncrypt(outputReflector)			
					secondOutputRe = self.secondRotor.postEncrypt(thirdOutputRe)					
					firstOutputRe = self.firstRotor.postEncrypt(secondOutputRe)				
					plugboardOutput = self.thePlugboard.changeString(firstOutputRe)					
					self.firstRotor.increment()

					# debugging output for -v
					debugLine+=" " + charUpper + "   "
					debugLine+= char + "         "
					debugLine+=firstOutput + "   "
					debugLine+=secondOutput + "   "
					debugLine+=thirdOutput + "   "
					debugLine+=outputReflector + "         "
					debugLine+=thirdOutputRe + "   "
					debugLine+=secondOutputRe + "   "
					debugLine+=firstOutputRe + "   "
					debugLine+=plugboardOutput + "         " + plugboardOutput + " "
					logging.debug(debugLine)

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
	runEnigma.readInput(sys.argv)






