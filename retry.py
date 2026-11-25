import sys
import time
from reader_shared import REVISION, fixture_record


def read(payload):
    print('Synthetic fixture revision: ' + str(REVISION), file=sys.stderr)
    not_before = float(payload.get('config', {}).get('not_before', 0))
    if time.time() < not_before:
        raise RuntimeError('Synthetic transient condition at revision ' + str(REVISION))
    return [fixture_record('retry')]
