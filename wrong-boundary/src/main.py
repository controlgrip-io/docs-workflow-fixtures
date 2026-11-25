import requests

def read(payload):
    return [{"stream": "users", "data": {"id": 1, "requests_version": requests.__version__}}]
