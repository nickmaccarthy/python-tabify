import os 
import sys
import unittest as unittest
import json
from pprint import pprint
import importlib

HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.append(HERE)

from tabify import tabify, print_as_json, TabifyException
import results 

class TestTabify(unittest.TestCase):
    def test_aggs(self):
        for item in results.agg_test_items:
            tabified = tabify(item['json_response'])
            expected = item['expected_result'] 
            self.assertItemsEqual(tabified, expected)

    def test_exceptions(self):
        self.assertRaises(TabifyException, tabify, '{ "omg": "this causes and exception"}')

    def test_hits_responses(self):
        for item in results.hits_test_items:
            tabified = tabify(item['json_response'])
            expected = item['expected_result'] 
            self.assertItemsEqual(tabified, expected)
        
if __name__ == "__main__":
    unittest.main()