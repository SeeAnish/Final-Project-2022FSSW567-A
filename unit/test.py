import unittest
from main import*

class Testmrz(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(vertify("W620126G54CIV5910106F9707302AJ010215I<<<<<<6"),"verification passed")
    def testcase2(self):
        self.assertEqual(vertify("V008493B64ABW7809095M0909088QZ181922T<<<<<<5"),"verification passed")
    def testcase3(self):
        self.assertEqual(vertify("L228735K44ZMB9104266F9603150KC823035R<<<<<<0"),"verification passed" )
    def testcase4(self):
        self.assertEqual(vertify("R810571G01GUF6208060F7411087QD954584R<<<<<<7"),"verification passed")
    def testcase5(self):
        self.assertAlmostEqual(vertify("M439232L64CRI7708268F9707069RD481066P<<<<<<6"),"verification passed")
    def testcase_passport_error_1(self):
        self.assertEqual(vertify("W620126G56CIV5910106F9707302AJ010215I<<<<<<6"),"passport info error")
    def testcase_passport_error_2(self):
        self.assertEqual(vertify("L228735K49ZMB9104266F9603150KC823035R<<<<<<0"),"passport info error")
    def testcase_passport_error_3(self):
        self.assertEqual(vertify("R810571G91GUF6208060F7411087QD954584R<<<<<<7"),"passport info error")
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()