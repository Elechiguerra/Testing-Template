### This is test_module1.py

import pytest
from package1.module1 import function_name, function_name1


class TestFunctionName:

    def test_function_name(self):

        assert boolean_expression [, message]  # message is displayed if AssertionError is raised

    def test_function_name(self):

        actual = function_name(argument)
        actual_type = type(actual)
        expected_type =
        expected =
        message1 = ('function_name(argument) returned type {0} instead of {1}'.format(actual_type, expected_type))
        message2 = ('function_name(argument) returned {0} instead of {1}'.format(actual, expected))

        assert expected_type == expected_type, message1
        assert actual is expected, message2


    def test_function_name_exception(self):

        with pytest.raises(ValueError): # any specific error type
            function_name(argument)
        ################ OR  ################
        with pytest.raises(ValueError) as exception_info: # any specific error type, to check if correct error message is returned
            expected_message = '    '
            function_name(argument)
            assert exception_info.match(expected_message)


    ## Whenever the test function needs a previous/posterior preparation
    @pytest.fixture
    def prepare_for_test():

        #SETUP

        with ... context manager... and yield output

        #TEARDOWN

    def test_function_name(self, prepare_for_test):

        input = prepare_for_test
        actual = function_name(input)

        assert boolean_expression [, message]  # message is displayed if AssertionError is raised


class TestFunctionName1:

    def test_function_name1(self):

        assert boolean_expression [, message]  # message is displayed if AssertionError is raised



# EXPECTED TO FAIL AND SKIPPED
"""
Use decorators above classes and functions to mark them as expected to fail (for
example if the function to test is not yet implemented), so they will not appear
as a failed test, or to skip them under a given condition that wiould make them
fail

    @pytest.mark.xfail / @pytest.mark.xfail(reason = 'why expected')
    @pytest.mark.skipif(boolean_expression [, reason = 'why skipped'])

To see the reasons of xfailing/skipping when testing:
    > pytest -rs/-rx/-rx

"""


# HOW TO RUN TESTS
"""
To run the test script *adapt to the corresponding script name*:
For IPython Shell or Notebooks, the command must start with --> !

Run test script in CWD
    > pytest test_template.py

Run all tests (being at -- cd tests --):
    > pytest

Run all tests until one fails (being at -- cd tests --):
    > pytest -x

Run test script, test class or test function
    > pytest package1/test_module1.py
    > pytest package1/test_module1.py::TestFunctionName
    > pytest package1/test_module1.py::TestFunctionName::test_function_name

Run specific test classes and functions by keyword
    > pytest -k 'TestFunctionName' and not '1'
    > pytest -k 'test_function_name'

"""

# DIRECTORY ORGANIZATION

    """
    src/ # Application directory
        package1/
            __init__.py
            module1.py           # Contains function_name(), function_name1()

        package2/
            __init__.py
            module2.py           # Contains function_name2()

    tests/ # Tests folder
        package1/
            __init__.py
            test_module1.py      # Corresponds to module src/package1/module1.py
        package2/
            __init__.py
            test_module2.py      # Corresponds to module src/package2/module2.py

    """
