import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise13(CustomTestCase):

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

    def test_all_digits_different(self):
        """
        All digits in the number are different.
        """
        inputs = ["1234"]
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_some_digits_same(self):
        """
        Some digits in the number are the same.
        """
        inputs = ["1123"]
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_all_digits_same(self):
        """
        All digits in the number are the same.
        """
        inputs = ["1111"]
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
