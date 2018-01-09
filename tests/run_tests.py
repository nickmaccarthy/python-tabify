import os 
import sys
import unittest as unittest
import json
from pprint import pprint
import importlib

S_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(S_HOME)

from tabify import tabify, print_as_json
import results 

class TestTabify(unittest.TestCase):
    def test_aggs(self):
        for item in results.test_items:
            tabified = tabify(item['json_response'])
            expected = item['expected_result'] 
            self.assertEqual(tabified, expected)
            try:
                self.assertEqual(tabified, expected)
            except Exception:
                print("items not equal: tabified_data:\n%s,\nexpected:\n%s" % (print_as_json(tabified), print_as_json(expected)))

if __name__ == "__main__":
    unittest.main()