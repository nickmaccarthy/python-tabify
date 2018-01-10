single_agg = """
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
"""
standard_hits = """
{
    "took": 1,
    "timed_out": false,
    "_shards":{
        "total" : 1,
        "successful" : 1,
        "skipped" : 0,
        "failed" : 0
    },
    "hits":{
        "total" : 1,
        "max_score": 1.3862944,
        "hits" : [
            {
                "_index" : "twitter",
                "_type" : "tweet",
                "_id" : "0",
                "_score": 1.3862944,
                "_source" : {
                    "user" : "kimchy",
                    "message": "trying out Elasticsearch",
                    "date" : "2009-11-15T14:12:12",
                    "likes" : 0
                }
            },
            {
                "_index" : "twitter",
                "_type" : "tweet",
                "_id" : "0",
                "_score": 3.00,
                "_source" : {
                    "user" : "someotheruser",
                    "message": "I love ES",
                    "date" : "2009-11-15T22:12:12",
                    "likes" : 30
                }
            }
        ]
    }
}
"""
double_terms_nested = '''
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 9,
    "successful": 9,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 0,
    "hits": [

    ]
  },
  "aggregations": {
    "error_msg": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 0,
      "buckets": [
        {
          "key": "bad juju",
          "doc_count": 1,
          "logstash_instance": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
              {
                "key": "logstash-shipper-plain",
                "doc_count": 1
              }
            ]
          }
        }
      ]
    }
  }
}
'''

events_by_status_code = """
{
  "took": 27,
  "timed_out": false,
  "_shards": {
    "total": 35,
    "successful": 35,
    "failed": 0
  },
  "hits": {
    "total": 564,
    "max_score": 0,
    "hits": []
  },
  "aggregations": {
    "status_code": {
      "doc_count_error_upper_bound": 0,
      "sum_other_doc_count": 4,
      "buckets": [
        {
          "key": 200,
          "doc_count": 186
        },
        {
          "key": 304,
          "doc_count": 41
        },
        {
          "key": 301,
          "doc_count": 40
        },
        {
          "key": 404,
          "doc_count": 6
        },
        {
          "key": 499,
          "doc_count": 5
        }
      ]
    }
  },
  "status": 200
}
"""

avg_response_time_by_endpoint = """
{
    "took": 142,
    "timed_out": false,
    "_shards": {
      "total": 3,
      "successful": 3,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 1180844,
      "max_score": 0,
      "hits": []
    },
    "aggregations": {
      "request_endpoint": {
        "doc_count_error_upper_bound": 0,
        "sum_other_doc_count": 424116,
        "buckets": [
          {
            "response_time_ms": {
              "value": 1219034
            },
            "key": "/weather/windsor",
            "doc_count": 1
          },
          {
            "response_time_ms": {
              "value": 108832.33333333333
            },
            "key": "/weather/waukasha",
            "doc_count": 6
          },
          {
            "response_time_ms": {
              "value": 163681
            },
            "key": "/weather/stamford",
            "doc_count": 1
          }
        ]
      }
    },
    "status": 200
  }
"""

percentiles_agg = """
{
    "took": 6938,
    "timed_out": false,
    "_shards": {
      "total": 3,
      "successful": 3,
      "skipped": 0,
      "failed": 0
    },
    "hits": {
      "total": 2143320,
      "max_score": 0,
      "hits": []
    },
    "aggregations": {
      "hostname": {
        "doc_count_error_upper_bound": 0,
        "sum_other_doc_count": 0,
        "buckets": [
          {
            "percentiles": {
              "values": [
                {
                  "key": 1,
                  "value": 200.00000000000003
                },
                {
                  "key": 5,
                  "value": 200
                },
                {
                  "key": 25,
                  "value": 200
                },
                {
                  "key": 50,
                  "value": 200
                },
                {
                  "key": 75,
                  "value": 200
                },
                {
                  "key": 95,
                  "value": 404
                },
                {
                  "key": 99,
                  "value": 500
                }
              ]
            },
            "key": "ip-10-229-86-192",
            "doc_count": 739474
          },
          {
            "percentiles": {
              "values": [
                {
                  "key": 1,
                  "value": 200.00000000000003
                },
                {
                  "key": 5,
                  "value": 200
                },
                {
                  "key": 25,
                  "value": 200
                },
                {
                  "key": 50,
                  "value": 200
                },
                {
                  "key": 75,
                  "value": 200.00000000000003
                },
                {
                  "key": 95,
                  "value": 408
                },
                {
                  "key": 99,
                  "value": 504
                }
              ]
            },
            "key": "ip-10-229-85-8",
            "doc_count": 231039
          },
          {
            "percentiles": {
              "values": [
                {
                  "key": 1,
                  "value": 200
                },
                {
                  "key": 5,
                  "value": 200
                },
                {
                  "key": 25,
                  "value": 200
                },
                {
                  "key": 50,
                  "value": 200
                },
                {
                  "key": 75,
                  "value": 200
                },
                {
                  "key": 95,
                  "value": 401
                },
                {
                  "key": 99,
                  "value": 500
                }
              ]
            },
            "key": "ip-10-229-81-27",
            "doc_count": 441370
          },
          {
            "percentiles": {
              "values": [
                {
                  "key": 1,
                  "value": 200
                },
                {
                  "key": 5,
                  "value": 200
                },
                {
                  "key": 25,
                  "value": 200
                },
                {
                  "key": 50,
                  "value": 200
                },
                {
                  "key": 75,
                  "value": 200
                },
                {
                  "key": 95,
                  "value": 404
                },
                {
                  "key": 99,
                  "value": 500
                }
              ]
            },
            "key": "ip-10-229-80-228",
            "doc_count": 731437
          }
        ]
      }
    },
    "status": 200
  }
"""

quad_nested_agg = """
{
    "took": 6,
    "timed_out": false,
    "_shards": {
      "total": 87,
      "successful": 87,
      "skipped": 84,
      "failed": 0
    },
    "hits": {
      "total": 3005,
      "max_score": 0,
      "hits": []
    },
    "aggregations": {
      "index_name": {
        "doc_count_error_upper_bound": -1,
        "sum_other_doc_count": 160,
        "buckets": [
          {
            "SizeOnDiskGB": {
              "value": 120
            },
            "Instances": {
              "value": 174
            },
            "Shards": {
              "value": 840
            },
            "DocCount": {
              "value": 302027752
            },
            "key": "microsoft-iis-",
            "doc_count": 5
          },
          {
            "SizeOnDiskGB": {
              "value": 107.4
            },
            "Instances": {
              "value": 30
            },
            "Shards": {
              "value": 120
            },
            "DocCount": {
              "value": 121569650
            },
            "key": "apache-httpd-",
            "doc_count": 5
          },
          {
            "SizeOnDiskGB": {
              "value": 15
            },
            "Instances": {
              "value": 174
            },
            "Shards": {
              "value": 840
            },
            "DocCount": {
              "value": 89146531
            },
            "key": "microsoft-iisxml-",
            "doc_count": 5
          }
        ]
      }
    },
    "status": 200
  }
"""


hits_agg = """
{
    "took": 30,
    "timed_out": false,
    "_shards": {
      "total": 84,
      "successful": 84,
      "skipped": 81,
      "failed": 0
    },
    "hits": {
      "total": 90113,
      "max_score": 0,
      "hits": []
    },
    "aggregations": {
      "top_tags": {
         "doc_count_error_upper_bound": 0,
         "sum_other_doc_count": 0,
         "buckets": [
            {
               "key": "hat",
               "doc_count": 3,
               "top_sales_hits": {
                  "hits": {
                     "total": 3,
                     "max_score": null,
                     "hits": [
                        {
                           "_index": "sales",
                           "_type": "sale",
                           "_id": "AVnNBmauCQpcRyxw6ChK",
                           "_source": {
                              "date": "2015/03/01 00:00:00",
                              "price": 200
                           },
                           "sort": [
                              1425168000000
                           ],
                           "_score": null
                        }
                     ]
                  }
               }
            },
            {
               "key": "t-shirt",
               "doc_count": 3,
               "top_sales_hits": {
                  "hits": {
                     "total": 3,
                     "max_score": null,
                     "hits": [
                        {
                           "_index": "sales",
                           "_type": "sale",
                           "_id": "AVnNBmauCQpcRyxw6ChL",
                           "_source": {
                              "date": "2015/03/01 00:00:00",
                              "price": 175
                           },
                           "sort": [
                              1425168000000
                           ],
                           "_score": null
                        }
                     ]
                  }
               }
            },
            {
               "key": "bag",
               "doc_count": 1,
               "top_sales_hits": {
                  "hits": {
                     "total": 1,
                     "max_score": null,
                     "hits": [
                        {
                           "_index": "sales",
                           "_type": "sale",
                           "_id": "AVnNBmatCQpcRyxw6ChH",
                           "_source": {
                              "date": "2015/01/01 00:00:00",
                              "price": 150
                           },
                           "sort": [
                              1420070400000
                           ],
                           "_score": null
                        }
                     ]
                  }
               }
            }
         ]
      }
    }
  }
"""

filters_agg = """
{
    "took": 30,
    "timed_out": false,
    "_shards": {
      "total": 84,
      "successful": 84,
      "skipped": 81,
      "failed": 0
    },
    "hits": {
      "total": 90113,
      "max_score": 0,
      "hits": []
    },
  "aggregations": {
    "messages": {
      "buckets": {
        "errors": {
          "doc_count": 1
        },
        "warnings": {
          "doc_count": 2
        },
        "other_messages": {
          "doc_count": 1
        }
      }
    }
  }
}
"""

sum_bucket_pipeline_agg = """
{
   "took": 11,
   "timed_out": false,
   "_shards": [],
   "hits": [],
   "aggregations": {
      "sales_per_month": {
         "buckets": [
            {
               "key_as_string": "2015/01/01 00:00:00",
               "key": 1420070400000,
               "doc_count": 3,
               "sales": {
                  "value": 550.0
               }
            },
            {
               "key_as_string": "2015/02/01 00:00:00",
               "key": 1422748800000,
               "doc_count": 2,
               "sales": {
                  "value": 60.0
               }
            },
            {
               "key_as_string": "2015/03/01 00:00:00",
               "key": 1425168000000,
               "doc_count": 2,
               "sales": {
                  "value": 375.0
               }
            }
         ]
      },
      "sum_monthly_sales": {
          "value": 985.0
      }
   }
}
"""

hits_test_items = [
  {
    "json_response": standard_hits,
    "expected_result": [
      {
        "user": "kimchy",
        "message": "trying out Elasticsearch",
        "date": "2009-11-15T14:12:12",
        "likes": 0
      },
      {
        "user": "someotheruser",
        "message": "I love ES",
        "date": "2009-11-15T22:12:12",
        "likes": 30
      }
    ]
  }
]

agg_test_items = [

    {
        "json_response": double_terms_nested,
        "expected_result": [
            {
            "error_msg": "bad juju",
            "logstash_instance": "logstash-shipper-plain",
            "doc_count": 1
            }
        ]
    },

    {
        "json_response": events_by_status_code,
        "expected_result": [
            {
            "status_code": 200,
            "doc_count": 186
            },
            {
            "status_code": 304,
            "doc_count": 41
            },
            {
            "status_code": 301,
            "doc_count": 40
            },
            {
            "status_code": 404,
            "doc_count": 6
            },
            {
            "status_code": 499,
            "doc_count": 5
            }
        ]
    },

    {
        "json_response": avg_response_time_by_endpoint,
        "expected_result": [ 
            { 
                "response_time_ms": 1219034,
                "request_endpoint": '/weather/windsor',
                "doc_count": 1 
            },
            { 
                "response_time_ms": 108832.33333333333,
                "request_endpoint": '/weather/waukasha',
                "doc_count": 6 
            },
            { 
                "response_time_ms": 163681,
                "request_endpoint": '/weather/stamford',
                "doc_count": 1 
            } 
        ]
    },

    {
        "json_response": percentiles_agg,
        "expected_result": [
            {
                "percentiles": 1,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 200.00000000000003
            },
            {
                "percentiles": 5,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 200
            },
            {
                "percentiles": 25,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 200
            },
            {
                "percentiles": 50,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 200
            },
            {
                "percentiles": 75,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 200
            },
            {
                "percentiles": 95,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 404
            },
            {
                "percentiles": 99,
                "hostname": "ip-10-229-86-192",
                "doc_count": 739474,
                "value": 500
            },
            {
                "percentiles": 1,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 200.00000000000003
            },
            {
                "percentiles": 5,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 200
            },
            {
                "percentiles": 25,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 200
            },
            {
                "percentiles": 50,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 200
            },
            {
                "percentiles": 75,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 200.00000000000003
            },
            {
                "percentiles": 95,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 408
            },
            {
                "percentiles": 99,
                "hostname": "ip-10-229-85-8",
                "doc_count": 231039,
                "value": 504
            },
            {
                "percentiles": 1,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 200
            },
            {
                "percentiles": 5,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 200
            },
            {
                "percentiles": 25,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 200
            },
            {
                "percentiles": 50,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 200
            },
            {
                "percentiles": 75,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 200
            },
            {
                "percentiles": 95,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 401
            },
            {
                "percentiles": 99,
                "hostname": "ip-10-229-81-27",
                "doc_count": 441370,
                "value": 500
            },
            {
                "percentiles": 1,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 200
            },
            {
                "percentiles": 5,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 200
            },
            {
                "percentiles": 25,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 200
            },
            {
                "percentiles": 50,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 200
            },
            {
                "percentiles": 75,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 200
            },
            {
                "percentiles": 95,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 404
            },
            {
                "percentiles": 99,
                "hostname": "ip-10-229-80-228",
                "doc_count": 731437,
                "value": 500
            }
        ]
    },

    {
        "json_response": quad_nested_agg,
        "expected_result": [
            {
                "SizeOnDiskGB": 120,
                "Instances": 174,
                "Shards": 840,
                "DocCount": 302027752,
                "index_name": "microsoft-iis-",
                "doc_count": 5
            },
            {
                "SizeOnDiskGB": 107.4,
                "Instances": 30,
                "Shards": 120,
                "DocCount": 121569650,
                "index_name": "apache-httpd-",
                "doc_count": 5
            },
            {
                "SizeOnDiskGB": 15,
                "Instances": 174,
                "Shards": 840,
                "DocCount": 89146531,
                "index_name": "microsoft-iisxml-",
                "doc_count": 5
            }
        ]
    },
    {
        "json_response": hits_agg,
        "expected_result": [
            {
                "top_tags": "hat",
                "doc_count": 3,
                "top_sales_hits": {
                "date": "2015/03/01 00:00:00",
                "price": 200,
                "sort": 1425168000000
                }
            },
            {
                "top_tags": "t-shirt",
                "doc_count": 3,
                "top_sales_hits": {
                "date": "2015/03/01 00:00:00",
                "price": 175,
                "sort": 1425168000000
                }
            },
            {
                "top_tags": "bag",
                "doc_count": 1,
                "top_sales_hits": {
                "date": "2015/01/01 00:00:00",
                "price": 150,
                "sort": 1420070400000
                }
            }
        ]
    },
    {
        "json_response": single_agg,
        "expected_result": [ { "queue_size": 138.0 } ]
    },
    {
        "json_response": filters_agg,
        "expected_result": [
            {
                "doc_count": 1,
                "messages": "errors"
            },
            {
                "doc_count": 2,
                "messages": "warnings"
            },
            {
                "doc_count": 1,
                "messages": "other_messages"
            }
        ]
    },
    {
        "json_response": sum_bucket_pipeline_agg,
        "expected_result": [
            {
                "sum_monthly_sales": 985.0
            }
        ]
    }
]












