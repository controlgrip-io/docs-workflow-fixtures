import requests
from reader_shared import fixture_record

def read(payload):
    return [fixture_record("nested-two", requests.__version__)]
