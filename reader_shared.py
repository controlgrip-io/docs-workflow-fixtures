REVISION = 2

def fixture_record(step, package_version=None):
    return {"stream": "users", "data": {"id": 1, "revision": REVISION, "step": step, "package_version": package_version}}
