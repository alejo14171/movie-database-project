import unittest
import sys
from pathlib import Path

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


def run_all_tests():
    """Run all tests in the 'tests' folder."""
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="tests", pattern="test_*.py")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n=== Test Summary ===")
    print(f"Total tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("\n=== Test Results ===")
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed or encountered errors.")


if __name__ == "__main__":
    run_all_tests()
