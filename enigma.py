# Enigma Program!
#
#  _______________________________ 
# < Enigma - by Christopher Jones >
#  ------------------------------- 
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||
# This is the main file for constructing and running the Enigma
# 



# The Enigma consists of 5 stages. 
# 1. The Keyboard: This implementation uses a standard 26-character alphabet
# 2. The Plugboard: Contains up to 13 mappings for characters output from the keyboard
# 3. The Rotors (part I) : Contains 3 rotors that individually offer a shift cipher, but move after every key press
#        resulting in a polyalphabetic cipher
# 4. The Reflector : Contains 13 character mappings to ensure the same character is not encoded to itself
# 5. The Rotors (part II) : Going in reverse order from part I, this time the rotors do not increment, used so
#        that the Enigma can be used to both encrypt and decrypt a message

from rotor import Rotor
from reflector import Reflector
import sys

print ""
print "---------------- Welcome to Enigma ----------------"
print "To encrypt a word, type 'encrypt' and then the word"
print "To exit, type 'exit'"
print "---------------------------------------------------"
print ""




# Set up 
firstRotor = Rotor()
secondRotor = Rotor()
thirdRotor = Rotor()
theReflector = Reflector()

firstRotor.setNextRotor(secondRotor)
secondRotor.setNextRotor(thirdRotor)

thirdRotor.setPreviousRotor(secondRotor)
secondRotor.setPreviousRotor(firstRotor)

firstRotor.changeTurnoverKey("R")
secondRotor.changeTurnoverKey("F")
thirdRotor.changeTurnoverKey("W")





# Start reading 

line = sys.stdin.readline()


while(line != "exit\n"):


	wordToEncrypt = None




	words = line.split()
	for word in words:

		if word == "encrypt":
	
			wordToEncrypt = words[1]

	if wordToEncrypt is not None and wordToEncrypt.isalpha():

		encryptedLength = len(wordToEncrypt)
		encryptedWord = ""


		for i in range(0,encryptedLength):

			char = wordToEncrypt[i]

			firstRotor.increment()
			firstOutput = firstRotor.encrypt(char)


			secondOutput = secondRotor.encrypt(firstOutput)
			thirdOutput = thirdRotor.encrypt(secondOutput)

			outputReflector = theReflector.getMapping(thirdOutput)


			thirdOutput = thirdRotor.postEncrypt(outputReflector)
			secondOutput = secondRotor.postEncrypt(thirdOutput)
			firstOutput = firstRotor.postEncrypt(secondOutput)

			encryptedWord += firstOutput


		print ""
		print wordToEncrypt, " encrypted as: ", encryptedWord
		print ""

		firstRotor.reset()
		secondRotor.reset()
		thirdRotor.reset()


	line = sys.stdin.readline()

















