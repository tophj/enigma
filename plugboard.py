# Plugboard. The plugboard connects the keyboard to the rotors. It is simply a mapping for 
# certain characters in the alphabet. The first and second versions of the Enigma used
# 10 plugs, or 20 character pairings. If a non paired character was selected, it would
# simply return itself.



class Plugboard:

	# Initialize default mapping
	# WZ AB MO TF RX SG QU VI YN EL
	def __init__(self):

		self.mapping = {
		'W':'Z', 'Z':'W',
		'A':'B', 'B':'A',
		'M':'O', 'O':'M',
		'T':'F', 'F':'T',
		'R':'X', 'X':'R',
		'S':'G', 'G':'S',
		'Q':'U', 'U':'Q',
		'V':'I', 'I':'V',
		'Y':'N', 'N':'Y',
		'E':'L', 'L':'E'}

	# returns the input strings mapping
	def changeString(self, string):

		returnString = ""
		for i in range(0,len(string)):
			char = string[i]
			if char in self.mapping.keys():
				returnString += self.mapping[char]
			else:
				returnString += char.upper()

		return returnString
