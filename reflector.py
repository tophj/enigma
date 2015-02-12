# Reflector
#
# The reflector contains a pairing for all alphabetical characters, this results
# in an encryption layer so that the starting character is never mapped to itself
#
import string


class Reflector:

	# Initialize mapping
	def __init__(self):

		# Default mapping for Reflector A. Using a dictionary for easy readibility
		# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
		# E  J  M  Z  A  L  Y  X  V  B  W  F  C  R  Q  U  O  N  T  S  P  I  K  H  G  D  

		self.mappingDict = {
		'A':'E', 'E':'A',
		'B':'J', 'J':'B',
		'C':'M', 'M':'C',
		'D':'Z', 'Z':'D',
		'F':'L', 'L':'F',
		'G':'Y', 'Y':'G',
		'H':'X', 'X':'H',
		'I':'V', 'V':'I',
		'K':'W', 'W':'K',
		'N':'R', 'R':'N',
		'O':'Q', 'Q':'O',
		'P':'U', 'U':'P',
		'S':'T', 'T':'S'}

	def getMapping(self, char):

		try:
			return self.mappingDict[char.upper()]
		except KeyError:
			print "Invalid character ", char, " entered into reflector"


