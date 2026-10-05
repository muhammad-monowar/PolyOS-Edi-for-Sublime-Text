"""Run every check: python3 -m tests.run

Exits non-zero if anything fails, so CI and pre-tag checks can rely on it.
"""

import sys

from tests import test_activate_profile, test_package_integrity

SUITES = (
    ("package structure", test_package_integrity.main),
    ("activate_profile behaviour", test_activate_profile.main),
)


def main():
    failed = []
    for title, run in SUITES:
        print("=" * 62)
        print(title)
        print("=" * 62)
        if run() != 0:
            failed.append(title)
        print()

    print("=" * 62)
    if failed:
        print("FAILED: " + ", ".join(failed))
        return 1
    print("All suites passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())