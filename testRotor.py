# Test for rotor.py


from rotor import Rotor


# Set up rotors
#
# 1st has turnover key A, starting char Z
# 2nd has turnover key R, starting char A (default)
# 3rd has turnover key A, starting char A

firstRotor = Rotor()
secondRotor = Rotor()
thirdRotor = Rotor()


firstRotor.setNextRotor(secondRotor)
secondRotor.setNextRotor(thirdRotor)

firstRotor.changeTurnoverKey("A")
thirdRotor.changeTurnoverKey("A")

firstRotor.changeStartingKey("Z")
thirdRotor.changeStartingKey("A")
print ""
print "Testing first rotor..."
if firstRotor.getStartingKey() != "Z":
	print "Starting key for first rotor is incorrect, it is :", firstRotor.getStartingKey()

if firstRotor.getTurnoverKey() != "A":
	print "Turnover key for second rotor is incorrect, it is :", firstRotor.getTurnoverKey()



print "Incrementing first rotor..."
# This should incrememnt the first rotor, which should also turnover the second rotor
firstRotor.increment()


if firstRotor.getStartingKey() != "A":
	print "Starting key for first rotor is incorrect, it is :", firstRotor.getStartingKey()


if secondRotor.getStartingKey() != "B":
	print "Starting key for second rotor is incorrect, it is :", secondRotor.getStartingKey()



#change startingKey to test encryption
print "Testing encrypt on first rotor..."

firstRotor.changeStartingKey("z")
testEncrypt1 = firstRotor.encrypt("A")
if testEncrypt1 != "Z":
	print "Encrypt is incorrect, it should be Z but instead is :", testEncrypt1



print "Done testing"

print ""