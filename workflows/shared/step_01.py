import os
import requests
from reader_shared import fixture_record

def read(payload):
    record = fixture_record("nested-one", requests.__version__)
    record["data"]["custom_path_preserved"] = "/reader-custom" in os.environ.get("PYTHONPATH", "").split(os.pathsep)
    return [record]
