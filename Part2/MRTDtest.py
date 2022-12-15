import time
import unittest
from HtmlTestRunner.runner import HTMLTestRunner
from MRTD import*

class Testmrz(unittest.TestCase):
    def testc1(self):
        string = "W620126G54CIV5910106F9707302AJ010215I<<<<<<6"
        self.assertEqual(algorithm(string[0:9]),4)
    def testc2(self):
        self.assertEqual(algorithm("ZE184226B"),1)
    def testc3(self):
        self.assertEqual(vertify("P<CIVL???N<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"),"contains invalid characters")
    def testcase1(self):
        self.assertEqual(vertify("P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<6"),"passed")
    def testcase2(self):
        self.assertEqual(vertify("P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<5"),"passed")
    def testcase3(self):
        self.assertEqual(vertify("P<ZMBROBERTSON<<ALINA<FERN<<<<<<<<<<<<<<<<<<;L228735K44ZMB9104266F9603150KC823035R<<<<<<0"),"passed" )
    def testcase4(self):
        self.assertEqual(vertify("P<GUFCAMACHO<<OSVALDO<ELODIE<<<<<<<<<<<<<<<<;R810571G01GUF6208060F7411087QD954584R<<<<<<7"),"passed")
    def testcase5(self):
        self.assertEqual(vertify("P<CRITYLER<<JANAE<<<<<<<<<<<<<<<<<<<<<<<<<<<;M439232L64CRI7708268F9707069RD481066P<<<<<<6"),"passed")
    def testcase_passport_error_1(self):
        self.assertEqual(vertify("P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G56CIV5910106F9707302AJ010215I<<<<<<6"),"passport info error")
    def testcase_passport_error_2(self):
        self.assertEqual(vertify("P<ZMBROBERTSON<<ALINA<FERN<<<<<<<<<<<<<<<<<<;L228735K49ZMB9104266F9603150KC823035R<<<<<<0"),"passport info error")
    def testcase_passport_error_3(self):
        self.assertEqual(vertify("P<GUFCAMACHO<<OSVALDO<ELODIE<<<<<<<<<<<<<<<<;R810571G91GUF6208060F7411087QD954584R<<<<<<7"),"passport info error")
    def testcase_birtherror_1(self):
        self.assertEqual(vertify("P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910102F9707302AJ010215I<<<<<<6"),"birth date info error")
    def testcase_birtherror_2(self):
        self.assertEqual(vertify("P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809091M0909088QZ181922T<<<<<<5"),"birth date info error")
    def testcase_birtherror_3(self):
        self.assertEqual(vertify("P<ZMBROBERTSON<<ALINA<FERN<<<<<<<<<<<<<<<<<<;L228735K44ZMB9104269F9603150KC823035R<<<<<<0"),"birth date info error")
    def testcase_vaiderror_1(self):
        self.assertEqual(vertify("P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707309AJ010215I<<<<<<6"),"validity info error")
    def testcase_vaiderror_2(self):
        self.assertEqual(vertify("P<ZMBROBERTSON<<ALINA<FERN<<<<<<<<<<<<<<<<<<;L228735K44ZMB9104266F9603158KC823035R<<<<<<0"),"validity info error")
    def testcase_vaiderror_3(self):
        self.assertEqual(vertify("P<GUFCAMACHO<<OSVALDO<ELODIE<<<<<<<<<<<<<<<<;R810571G01GUF6208060F7411081QD954584R<<<<<<7"),"validity info error")
    def testcase_personalcodeerror_1(self):
        self.assertEqual(vertify("P<CIVLYNN<<NEVEAH<BRAM<<<<<<<<<<<<<<<<<<<<<<;W620126G54CIV5910106F9707302AJ010215I<<<<<<8"),"personal code error")
    def testcase_personalcodeerror_2(self):
        self.assertEqual(vertify("P<ABWMALDONADO<<CAMILLA<<<<<<<<<<<<<<<<<<<<<;V008493B64ABW7809095M0909088QZ181922T<<<<<<6"),"personal code error")
    def testcase_personalcodeerror_3(self):
        self.assertEqual(vertify("P<ZMBROBERTSON<<ALINA<FERN<<<<<<<<<<<<<<<<<<;L228735K44ZMB9104266F9603150KC823035R<<<<<<7"),"personal code error")

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Testmrz))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    runner = HTMLTestRunner(verbosity=2, output='Report', report_name='Unit Test', open_in_browser=True)
    runner.run(suite)

if __name__ == '__main__':
    print('Running unit tests')
    main()
