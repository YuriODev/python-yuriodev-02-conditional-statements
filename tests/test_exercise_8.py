import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise8(CustomTestCase):

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

    def test_digit_in_number(self):
        """
        Digit is in the number.
        """
        inputs = ["123", "2"]
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_digit_not_in_number(self):
        """
        Digit is not in the number.
        """
        inputs = ["456", "2"]
        output = self.run_exercise(inputs)
        expected_output = "False"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_digit_in_number_2(self):
        """
        Digit is in the number.
        """
        inputs = ["123", "3"]
        output = self.run_exercise(inputs)
        expected_output = "True"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
