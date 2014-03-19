# Plugboard. The plugboard connects the keyboard to the rotors. It is simply a mapping for 
# certain characters in the alphabet. The first and second versions of the Enigma used
# 10 plugs, or 20 character pairings. If a non paired character was selected, it would
# simply return itself.



class Plugboard:

	# Initialize default mapping
	# WZ AB MO TF RX SG QU VI YN EL
	def __init__(self):

		self.mapping = {'W' : 'Z',
		'A':'B',
		'M':'O',
		'T':'F',
		'R':'X',
		'S':'G',
		'Q':'U',
		'V':'I',
		'Y':'N',
		'E':'L',

		'Z':'W',
		'B':'A',
		'O':'M',
		'F':'T',
		'X':'R',
		'G':'S',
		'U':'Q',
		'I':'V',
		'N':'Y',
		'L':'E'}
		


	def changeString(self, string):

		for i in range(0,len(string)):

			char = string[i]

			if char in self.mapping.keys():
				char = self.mapping[char]



		return string
