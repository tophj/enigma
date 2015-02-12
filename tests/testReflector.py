import unittest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from reflector import Reflector


class testReflector(unittest.TestCase):

	def setUp(self):
		self.reflector = Reflector()

	# To test for mistypes
	def test_getMapping(self):


		self.assertEqual(self.reflector.getMapping("A"),"E")
		self.assertEqual(self.reflector.getMapping("B"),"J")
		self.assertEqual(self.reflector.getMapping("C"),"M")
		self.assertEqual(self.reflector.getMapping("D"),"Z")
		self.assertEqual(self.reflector.getMapping("E"),"A")
		self.assertEqual(self.reflector.getMapping("F"),"L")
		self.assertEqual(self.reflector.getMapping("G"),"Y")
		self.assertEqual(self.reflector.getMapping("H"),"X")
		self.assertEqual(self.reflector.getMapping("I"),"V")
		self.assertEqual(self.reflector.getMapping("J"),"B")
		self.assertEqual(self.reflector.getMapping("k"),"W")
		self.assertEqual(self.reflector.getMapping("L"),"F")
		self.assertEqual(self.reflector.getMapping("M"),"C")
		self.assertEqual(self.reflector.getMapping("N"),"R")
		self.assertEqual(self.reflector.getMapping("O"),"Q")
		self.assertEqual(self.reflector.getMapping("P"),"U")
		self.assertEqual(self.reflector.getMapping("Q"),"O")
		self.assertEqual(self.reflector.getMapping("R"),"N")
		self.assertEqual(self.reflector.getMapping("s"),"T")
		self.assertEqual(self.reflector.getMapping("t"),"S")
		self.assertEqual(self.reflector.getMapping("U"),"P")
		self.assertEqual(self.reflector.getMapping("v"),"I")
		self.assertEqual(self.reflector.getMapping("W"),"K")
		self.assertEqual(self.reflector.getMapping("X"),"H")
		self.assertEqual(self.reflector.getMapping("y"),"G")
		self.assertEqual(self.reflector.getMapping("z"),"D")


if __name__ == "__main__":
    unittest.main()