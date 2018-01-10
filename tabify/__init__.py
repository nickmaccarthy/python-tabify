"""
tabify module

Emulates the Kibana Tabify module that flattens nested Elasticsearch responses into a consumable dictionary for use in things like HTML tables or other graphic engines


Usage:
from tabify import tabify

# this emulates a JSON response we would get back from Elasticsearch
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
"""
import json
from functools import reduce
from pprint import pprint
from pprint import pformat
import logging 
import copy 

logging.basicConfig(format="%(asctime)s - %(name)s - [ %(levelname)s ] - [ %(filename)s:%(funcName)s():%(lineno)s ] - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

def print_as_json(object):
    ''' pretty prints an object as JSON '''
    item = json.dumps(list(object), indent=4, sort_keys=False)
    return item

class TabifyException(Exception):
    pass 
        
def tabify(response, **options):
    table = []
    # If we dont have converted JSON object, lets try to do that first
    if not isinstance(response, dict):
        try:
            response = json.loads(response)
        except TabifyException as e:
            raise TabifyException("Unable to convert response to JSON, reason: %s, please ensure you are sending either valid JSON or a python DICT to this method" % (e))

    logger.debug("Our response:\n%s" % print_as_json(response))

    if response.get("aggregations"):
        tree = collectBucket(response["aggregations"])
        logger.debug("tabify tree:\n%s" % print_as_json(tree)) 
        table_items = flatten(tree)
        
        logger.debug("table_items len: %s" % len(table_items))
        logger.debug("table_items:\n%s" % (print_as_json(table_items)))

        if len(table_items) > 1:
            for items in table_items:
                logger.debug("items len in for loop: %s" % (len(items)))

                if isinstance(items, list):
                    logger.debug("items is a list: %s" % (items))
                    for item in items:
                        logger.debug("item: %s" % (item))
                        table.append(item)
                else:
                    table.append(items)

        if len(table_items) == 1:
            logger.debug("we have 1 item in table_items:\n%s" % (print_as_json(table_items)))
            if isinstance(table_items[0], list):
                for item in table_items[0]:
                    table.append(item)
            else:
                table.append(table_items[0])
    elif isinstance(response.get('hits'), dict):
        for hit in response['hits']['hits']:
            table.append(hit['_source'])

    elif isinstance(response, list):
        table = response 
    
    else:
        raise TabifyException("Tabify() invalid response. Result set must have either 'aggregations' or 'hits' defined.")

    logger.debug("here now...I am returning table: %s" % table)

    return table

def collectBucket(node, stack=[]):
    if not node:
        return
    
    keys = node.keys() 

    for i, key in enumerate(keys):
        value = node[key]
        
        if isinstance(value, dict) or isinstance(value, list) and value:
            logger.debug("key: %s, value: %s" % (key, value))

            if isinstance(value, dict) and value.get('value'):
                return { key: value['value'] }
            
            if "hits" in key and value.get('hits') and len(value.get('hits')) == 1:
                ourd = value["hits"][0]
                if "sort" in ourd:
                    ourd["_source"]["sort"] = ourd["sort"][0]
                return ourd['_source']

            if isinstance(value, list):
                nstack = list(stack)
                nstack.append(key)
                return extractTree(value, nstack)

            if "buckets" in key and len(value.keys()) > 1:
                logger.debug("found my key to be buckets")
                nstack = list(stack)
                nstack.append(key)
                return extractBuckets(value, nstack)

            nstack = list(stack)
            nstack.append(key)
            logger.debug("re-running collectBucket()")
            return collectBucket(value, nstack)
    
    return node

def extractBuckets(buckets, stack):
    keys = buckets.keys() 
    results = [] 
    for i, key in enumerate(buckets):
        value = buckets[key]

        currentObject = collectBucket({key: value})

        if not currentObject:
            continue 
    
        currentObject[stack[len(stack) - 2]] = key 
        results.append(currentObject)
    return results 

def extractTree(buckets, stack):
    logger.debug("buckets len: %s" % len(buckets))
    logger.debug("buckets:\n%s" % (print_as_json(buckets)))
    items = []
    for bucket in buckets:
        logger.debug("bucket:\n%s" %(bucket))
        tree = {}
        for key in bucket.keys():
            value = bucket[key]
            if isinstance(value, dict):
                if "value" in value:
                    logger.debug("got a value!")
                    value = value["value"]
                    logger.debug("found a value: stack: %s, value: %s" % (stack,value))
                else: 
                    nstack = list(stack)
                    nstack.append(key) 
                    value = collectBucket(value, nstack)
            if key == "key":
                key = stack[len(stack) - 2]
            logger.debug("loop key: %s, value: %s" % (key, value))
            if key == "value" and len(stack) == 1:
                key = stack[0]
                 
            tree[key] = value
        items.append(tree)
    return items


def flatten(tree, parentNode={}):
    if not tree:
        return []

    if not isinstance(tree, list):
       tree = [tree]

    for i, childNode in enumerate(tree):
        temp = copy.deepcopy(parentNode)
        temp.update(childNode)
        tree[i] = temp

    logger.debug("flatten tree, with child pairs: %s" % (print_as_json(tree)))  
    logger.debug("tree len : %s" % (len(tree))) 

    for i, node in enumerate(tree):
        logger.debug("node: %s" % node)  
        logger.debug("node keys: %s" % (print_as_json(node.keys())))

        possibleChildTrees = node.keys()

        logger.debug("possibleChildTrees : %s" % (print_as_json(possibleChildTrees)))
        
        childTrees = []
        for el in possibleChildTrees:
            if isinstance(node[el], list) or isinstance(node[el], dict):
                childTrees.append(node[el])

        logger.debug("childTrees : length: %s, extract: %s" % (len(childTrees), print_as_json(childTrees)))

        if len(childTrees) == 0:
            logger.debug("childTrees len == 0")
            tree[i] = node 
        elif len(childTrees) == 1: 
            logger.debug("chilTrees len == 1")
            childTree = childTrees[0]
            logger.debug("childTree:\n%s" % (print_as_json(childTree)))
            if len(childTree) == 0:
                logger.debug("childTree len == 0")
                tree[i] = node 
            else: 
                if isinstance(childTree, dict):
                    logger.debug("childTree isinstance == dict")
                    tree[i] = node 
                else:
                     logger.debug("childTree type test is default")
                     logger.debug("sending the following to flatten() :\n childTree:\n%s,\nnode:%s\n" % (print_as_json(childTree), print_as_json(node)))
                     tree[i] = flatten(childTree, node)
        else:
            logger.debug("!!!!! We shouldnt be here!!")
            raise TabifyException("We shouldnt be here!")

    logger.debug("flatten tree:\n%s" % print_as_json(tree))
    return tree

