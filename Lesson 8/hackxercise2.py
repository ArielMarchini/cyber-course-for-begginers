import requests
import json


def get():
    res = requests.get('http://httpbin.org/status/204')
    return res.status_code

def post():
    res = requests.post('http://httpbin.org/post', {"x": 1, "y": 2})
    return res.status_code



