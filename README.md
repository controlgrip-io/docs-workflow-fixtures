# ControlGrip strict-reader public runtime fixtures

Contains no credentials, customer data, or ControlGrip implementation code. Built solely from public cookbook protocol contracts.

- Root Python: workdir `.`, main file `main.py`, entrypoint `read`, users/id contract min 1.
- Nested Python: workdir `workflows/shared`, main files `step_01.py` and `step_02.py`, entrypoint `read`. Both import repository-root module and requests from the exact workdir manifest. Optional organization variable binding PYTHONPATH=/reader-custom verifies preservation without credentials.
- Wrong boundary negative: workdir `wrong-boundary`, main `src/main.py`. Requirements only next to main must NOT be installed. Expected import failure on a clean Python image without requests.
- pyproject negative: workdir `pyproject-only`, main `main.py`. pyproject dependencies must NOT be auto-installed; same clean-image prerequisite.
- TypeScript: workdir `typescript`, main `main.ts`, entrypoint `read`.

To advance the branch, change REVISION in reader_shared.py from 1 to 2 and commit. Tracking runs should record the new commit; historical and pin-policy runs must keep the old commit. Revert that change as a new commit for rollback tests.

Native Git tasks: workdir `bin`, main `golang` or `rust`, Linux amd64 static executables; sources are in native-src. Step one supports config.require_custom_path=true to require the documented custom PYTHONPATH entry.
