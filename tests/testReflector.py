import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from reflector import Reflector

# Reflector settings
# {'A' : 'Z',
# 		'B':'Y',
# 		'C':'X',
# 		'D':'W',
# 		'E':'V',
# 		'F':'U',
# 		'G':'T',
# 		'H':'S',
# 		'I':'R',
# 		'J':'Q',
# 		'K':'P',
# 		'L':'O',
# 		'M':'N',
# 		'N':'M',
# 		'O':'L',
# 		'P':'K',
# 		'Q':'J',
# 		'R':'I',
# 		'S':'H',
# 		'T':'G',
# 		'U':'F',
# 		'V':'E',
# 		'W':'D',
# 		'X':'C',
# 		'Y':'B',
# 		'Z':'A',
# 		}

class testReflector(unittest.TestCase):

	def setUp(self):
		self.reflector = Reflector()

	# To test for mistypes
	def test_getMapping(self):


		self.assertEqual(self.reflector.getMapping("A"),"Z")
		self.assertEqual(self.reflector.getMapping("B"),"Y")
		self.assertEqual(self.reflector.getMapping("C"),"X")
		self.assertEqual(self.reflector.getMapping("D"),"W")
		self.assertEqual(self.reflector.getMapping("E"),"V")
		self.assertEqual(self.reflector.getMapping("F"),"U")
		self.assertEqual(self.reflector.getMapping("G"),"T")
		self.assertEqual(self.reflector.getMapping("H"),"S")
		self.assertEqual(self.reflector.getMapping("I"),"R")
		self.assertEqual(self.reflector.getMapping("J"),"Q")
		self.assertEqual(self.reflector.getMapping("k"),"P")
		self.assertEqual(self.reflector.getMapping("L"),"O")
		self.assertEqual(self.reflector.getMapping("M"),"N")
		self.assertEqual(self.reflector.getMapping("N"),"M")
		self.assertEqual(self.reflector.getMapping("O"),"L")
		self.assertEqual(self.reflector.getMapping("P"),"K")
		self.assertEqual(self.reflector.getMapping("Q"),"J")
		self.assertEqual(self.reflector.getMapping("R"),"I")
		self.assertEqual(self.reflector.getMapping("s"),"H")
		self.assertEqual(self.reflector.getMapping("t"),"G")
		self.assertEqual(self.reflector.getMapping("U"),"F")
		self.assertEqual(self.reflector.getMapping("v"),"E")
		self.assertEqual(self.reflector.getMapping("W"),"D")
		self.assertEqual(self.reflector.getMapping("X"),"C")
		self.assertEqual(self.reflector.getMapping("y"),"B")
		self.assertEqual(self.reflector.getMapping("z"),"A")


if __name__ == "__main__":
    unittest.main()