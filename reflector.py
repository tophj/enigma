# Reflector
#
# The reflector contains a pairing for all alphabetical characters, this results
# in an encryption layer so that the starting character is never mapped to itself
#
import string


class Reflector:

	# Initialize mapping
	def __init__(self, version=None):

		# Default mapping for Reflector A. Using a dictionary for easy readibility
		# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
		# E  J  M  Z  A  L  Y  X  V  B  W  F  C  R  Q  U  O  N  T  S  P  I  K  H  G  D  

		# Default mapping for Reflector B. Using a dictionary for easy readibility
		# A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
		# Y  R  U  H  Q  S  L  D  P  X  N  G  O  K  M  I  E  B  F  Z  C  W  V  J  A  T

		if(version is 'B'):
			# Reflector B
			self.mappingDict = {
			'A':'Y', 'Y':'A',
			'B':'R', 'R':'B',
			'C':'U', 'U':'C',
			'D':'H', 'H':'D',
			'E':'Q', 'Q':'E',
			'F':'S', 'S':'F',
			'G':'L', 'L':'G',
			'I':'P', 'P':'I',
			'J':'X', 'X':'J',
			'N':'K', 'K':'N',
			'O':'M', 'M':'O',
			'V':'W', 'W':'V',
			'Z':'T', 'T':'Z'}
		else:
			# Reflector A
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


