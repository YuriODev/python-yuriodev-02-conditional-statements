import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise14(CustomTestCase):

    def test_list_usage(self):
        """
        The program should not use lists to solve the exercise.
        """
        self.assertNotUsesList()

    def test_dict_usage(self):
        """
        The program should not use dictionaries to solve the exercise.
        """
        self.assertNoUsesDictionary()

    def test_function_usage(self):
        """
        The program should not use functions to solve the exercise.
        """
        self.assertNotUseSelfDefinedFunctions()

    def test_palindrome_number_true(self):
        """
        Number is a palindrome.
        """
        inputs = ["1221"]
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_palindrome_number_false(self):
        """
        Number is not a palindrome.
        """
        inputs = ["1234"]
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_palindrome_number_2(self):
        """
        Number is a palindrome.
        """
        inputs = ["1331"]
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
