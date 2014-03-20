# Reflector
#
# The reflector contains a pairing for all alphabetical characters, this results
# in an encryption layer so that the starting character is never mapped to itself
#
import string


class Reflector:



	# Initialize mapping
	def __init__(self):

		# Default mapping. Using a dictionary for easy readibility
		self.mappingDict = {'A' : 'Z',
		'B':'Y',
		'C':'X',
		'D':'W',
		'E':'V',
		'F':'U',
		'G':'T',
		'H':'S',
		'I':'R',
		'J':'Q',
		'K':'P',
		'L':'O',
		'M':'N',
		'N':'M',
		'O':'L',
		'P':'K',
		'Q':'J',
		'R':'I',
		'S':'H',
		'T':'G',
		'U':'F',
		'V':'E',
		'W':'D',
		'X':'C',
		'Y':'B',
		'Z':'A',
		}


	def getMapping(self, char):

		try:
			return self.mappingDict[char.upper()]

		except KeyError:

			print "Invalid character ", char, " entered into reflector"





