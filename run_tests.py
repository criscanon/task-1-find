import unittest
import coverage

def run_tests():
    """
    Run unit tests using the unittest framework with coverage.

    Returns:
        Coverage object: The coverage object after running the tests.
    """
    # Start code coverage
    cov = coverage.Coverage()
    cov.start()

    # Discover and load all tests from the 'tests' directory
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')

    # Run the tests
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    # Stop code coverage
    cov.stop()

    # Output the result of the tests
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print(f"{result.errors} errors and {result.failures} failures occurred.")

    # Generate and print coverage report
    cov.report()

    return cov

if __name__ == '__main__':
    coverage_object = run_tests()
