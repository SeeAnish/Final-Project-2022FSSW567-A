import json
import unittest
from checker import*

class Testmrz(unittest.TestCase):
    def testcase1(self):
        with open('records_encoded.json') as json_file:
            data = json.load(json_file)
            records = data["records_encoded"]
            for i in range(0, 100):
                print(records[i])
                self.assertEqual(vertify(records[i]),"passed")        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()