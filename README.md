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

Now lets look at a deeper, more nested aggregation and make an HTML table from our Tabify results:
```
from tabify import tabify 

double_terms_nested = '''
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 39,
    "successful": 39,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 50,
    "max_score": 0,
    "hits": []
  },
  "aggregations": {
    "error_message": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "instance_type": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
              {
                "key": "logstash-shipper-plain",
                "doc_count": 36
              }
            ]
          },
          "key": "Uh ohs; you should really look into this one",
          "doc_count": 36
        },
        {
          "instance_type": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
              {
                "key": "logstash-receiver-plain",
                "doc_count": 1
              },
              {
                "key": "logstash-shipper-plain",
                "doc_count": 1
              }
            ]
          },
          "key": "Oh noes, another bad error",
          "doc_count": 2
        }
      ]
    }
  },
  "status": 200
}
'''

# Tabify our aggregation response
tabified = tabify(double_terms_nested)

# build our headers for our table
headers = tabified[0].keys()

# Build the HTML table
table = []
theaders = []
for h in headers:
    theaders.append("<th>%s</th>" % h)

table.append("<table border='1' cellpadding='1' cellspacing='1'>")
table.append("<thead>")
table.append("<tr>")
for h in headers:
    table.append("<th>%s</th>" % h)
table.append("</tr>")
table.append("</thead>")

table.append("<tbody>")
tblst = []
for l in tabified:
    table.append("<tr>")
    for h in headers:
        table.append("<td><pre> %s </pre></td>" % (str(l[h])))
    table.append("</tr>")
table.append("</tbody>")
table.append("</table>")

html_table = ''.join(table)

# Print out our HTML table
try: 
  from bs4 import BeautifulSoup
  soup = BeautifulSoup(html_table, 'html.parser')
  prettyHTML = soup.prettify()
  print(prettyHTML)
except Exception as e:
  print("Unable to find bs4, printing non-pretty html table %s" % (e))
  print html_table

```

The above would generate html for a table:
```
<table border="1" cellpadding="1" cellspacing="1">
 <thead>
  <tr>
   <th>
    instance_type
   </th>
   <th>
    error_message
   </th>
   <th>
    doc_count
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    <pre> logstash-shipper-plain </pre>
   </td>
   <td>
    <pre> Uh ohs; you should really look into this one </pre>
   </td>
   <td>
    <pre> 36 </pre>
   </td>
  </tr>
  <tr>
   <td>
    <pre> logstash-receiver-plain </pre>
   </td>
   <td>
    <pre> Oh noes, another bad error </pre>
   </td>
   <td>
    <pre> 1 </pre>
   </td>
  </tr>
  <tr>
   <td>
    <pre> logstash-shipper-plain </pre>
   </td>
   <td>
    <pre> Oh noes, another bad error </pre>
   </td>
   <td>
    <pre> 1 </pre>
   </td>
  </tr>
 </tbody>
</table>

```

Which should render out to a table that looks like:

| instance_type | error_message | doc_count |
|--- |--- |--- |
|logstash-shipper-plain|Uh ohs; you should really look into this one|36|
|logstash-receiver-plain|Oh noes, another bad error|1|
|logstash-shipper-plain|Oh noes, another bad error|1|

# Tests
```
python tests/run_tests.py 
```

# Versions
* 1.0 - Initial Version

# Contrubuiting your changes
1. Git clone this repo
    * `git clone https://github.com/nickmaccarthy/python-tabify`
2. Create a branch for your work
    * `git checkout -b my-branch-name`
3. Make your changes
4. Add your tests to to `tests/run_tests.py`
5. Verify your tests run in both python 2 and 3
    * `python2.7 tests/run_tests.py`
    * `python3 tests/run_tests.py`
6. Make a pull request on GitHub

# License 
MIT 

# Python Version Supprt
* 2.7
* 3.2
* 3.3
* 3.4
* 3.5
* 3.6

* 2.6 *note* python v2.6 is not suppored in CI.  While I have tested it working manually, I can't guarantee future support 

# Known Issues 
* Pipeline aggregations will only return the sum bucket.  To be fair, pipeline aggs dont work in the Kibana viz tool at this time so its hard to test it with Kibana tabify

# Credits
* [es-tabify](https://github.com/datavis-tech/es-tabify) 
* [Kibana's Graphing Implementation](https://github.com/elastic/kibana/tree/master/src/ui/public/agg_response/tabify)
* [Mr Neas](https://github.com/michaelneas)