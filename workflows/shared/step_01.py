import os
import requests
from reader_shared import fixture_record

def read(payload):
    record = fixture_record("nested-one", requests.__version__)
    record["data"]["custom_path_preserved"] = "/reader-custom" in os.environ.get("PYTHONPATH", "").split(os.pathsep)
    if payload.get("config", {}).get("require_custom_path"):
        assert record["data"]["custom_path_preserved"], "custom PYTHONPATH was not preserved"
    return [record]
