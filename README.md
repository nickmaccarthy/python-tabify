[![Build Status](https://travis-ci.org/nickmaccarthy/python-tabify.svg?branch=master)](https://travis-ci.org/nickmaccarthy/python-tabify.svg?branch=master)
# tabify
A python module that emulates the Kibana tabify method that converts nested Elasticsearch JSON responses into a consumable data structure.  The returned data is a list of dictionaries which can be used to easily build HTML tables or other graphing engines.  

Inspired by [Kibana's Graphing Implementation](https://github.com/elastic/kibana/tree/master/src/ui/public/agg_response/tabify) and the [es-tabify](https://github.com/datavis-tech/es-tabify) node module.  

# Usage
First, install it: 
```
pip install tabify
```

Now lets try it out:
```
from tabify import tabify 

# Emulate a JSON response from Elasticsearch
single_agg = '''
{
    "hits": {
        "hits": [],
        "total": 19,
        "max_score": 0.0
    },
    "_shards": {
        "successful": 10,
        "failed": 0,
        "total": 10
    },
    "took": 10,
    "aggregations": {
        "queue_size": {
            "value": 138.0
        }
    },
    "timed_out": false
}
'''

tabified = tabify(single_agg)

# A helper function to pretty print our return as JSON
from tabify import print_as_json

print_as_json(tabified)
>>> 
[
    {
        "queue_size": 138.0
    }
]
```

# Tests
```
python tests/run_tests.py 
```


# License 
MIT 

# Python Versions
* 2.6
* 2.7
* 3.4
* 3.5
* 3.6

# Credits
* [es-tabify](https://github.com/datavis-tech/es-tabify) 
* [Kibana's Graphing Implementation](https://github.com/elastic/kibana/tree/master/src/ui/public/agg_response/tabify)