






from rotor import Rotor
from reflector import Reflector
import sys

firstRotor = Rotor()
secondRotor = Rotor()
thirdRotor = Rotor()
theReflector = Reflector()

firstRotor.setNextRotor(secondRotor)
secondRotor.setNextRotor(thirdRotor)

thirdRotor.setPreviousRotor(secondRotor)
secondRotor.setPreviousRotor(firstRotor)





char = sys.stdin.read(1)
while(char != "!"):
#for char in sys.stdin.read(1):

	if char.isalpha():
		char = char.upper()


		firstRotor.increment()
		firstOutput = firstRotor.encrypt(char)


		secondOutput = secondRotor.encrypt(firstOutput)
		thirdOutput = thirdRotor.encrypt(secondOutput)

		outputReflector = theReflector.getMapping(thirdOutput)


		thirdOutput = thirdRotor.postEncrypt(outputReflector)
		secondOutput = secondRotor.postEncrypt(thirdOutput)
		firstOutput = firstRotor.postEncrypt(secondOutput)

		print char, "is encoded as : ", firstOutput 
		#char = sys.stdin.read(1)

	elif char is '\n' or " ":
		pass
	else:
		print "Input can only be a letter."
		

	char = sys.stdin.read(1)

		



