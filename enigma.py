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

firstRotor = Rotor()
secondRotor = Rotor()
thirdRotor = Rotor()
theReflector = Reflector()

firstRotor.setNextRotor(secondRotor)
secondRotor.setNextRotor(thirdRotor)

thirdRotor.setPreviousRotor(secondRotor)
secondRotor.setPreviousRotor(firstRotor)

