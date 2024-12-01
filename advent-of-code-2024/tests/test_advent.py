from advent import *

class AdventTest(unittest.TestCase):

    def testBoolListToDecimal(self):
        self.assertEqual(11, bool_list_to_decimal([1, 0, 1, 1]))
        
    def testFileToLines(self):
        lines = file_to_lines("tests/test_advent.py")
        self.assertEqual("from advent import *", lines[0])

    def testFindF(self):
        first_pos = findf(lambda n :  n > 0, [ -3, -4, -7, 5, 4, 3 ])
        self.assertEqual(5, first_pos)
        
    def testIterate(self):
        thrice_squared = iterate(lambda n : n * n, 7, 3)
        self.assertEqual(5764801, thrice_squared)
        
    def testPartition(self):
        pos, neg = partition([1, 4, -7, 5, -9, -1], lambda n : n >= 0)
        self.assertEqual([1, 4, 5], pos)
        self.assertEqual([-7, -9, -1], neg)

    # Peter Norvig's functions ----------------------------------------------------------------

    def testAtom(self):
        self.assertEqual(7, atom(" 7 "))
        self.assertEqual(" s ", atom(" s "))
        
    def testAtoms(self):
        self.assertEqual((7, "foo", "bar", 9.8), atoms(" 7,foo   bar: 9.8 "))
        
    def testDigits(self):
        self.assertEqual((3, 1, 4, 2, 7, 1, 8), digits("3.14 is pi, 2.718 is e"))

    def testInts(self):
        self.assertEqual((3, 14, 2, 718), ints("3.14 is pi, 2.718 is e"))
        
    def testMapt(self):
        squares = mapt(lambda n : n * n, [ 1, 2, 3 ])
        self.assertEqual((1, 4, 9), squares)

    def testQuantify(self):
        self.assertEqual(3, quantify([1, 2, 3, 4, 5, 6, 8], lambda n : (n % 2) != 0))
        
    def testTrunc(self):
        self.assertEqual("beg ... end", trunc("beginning to the end", left=3, right=3))

    def testWords(self):
        self.assertEqual(["one", "two", "three", "MixedCase"],
                         words("one, two...three MixedCase"))

if __name__=='__main__':
    unittest.main()
