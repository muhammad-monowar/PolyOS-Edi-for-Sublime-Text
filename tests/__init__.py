"""Put the stub modules and the package root on sys.path.

The package root is on the path because the package *is* the repo root, so
`import activate_profile` has to resolve there the same way Sublime resolves
it once the package is installed.
"""

import os
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(TESTS_DIR)
STUBS_DIR = os.path.join(TESTS_DIR, "stubs")

# stubs first: they must shadow anything real, and there is nothing real here.
if STUBS_DIR not in sys.path:
    sys.path.insert(0, STUBS_DIR)
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)