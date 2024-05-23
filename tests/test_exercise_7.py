import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise7(CustomTestCase):

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

    def test_addition(self):
        """
        Test addition operation.
        """
        inputs = ["5", "3", "+"]
        output = self.run_exercise(inputs)
        expected_output = "8.0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_division_by_zero(self):
        """
        Test division by zero.
        """
        inputs = ["5", "0", "/"]
        output = self.run_exercise(inputs)
        expected_output = "Division by 0!"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_multiplication(self):
        """
        Test multiplication operation.
        """
        inputs = ["5", "3", "*"]
        output = self.run_exercise(inputs)
        expected_output = "15.0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_subtraction(self):
        """
        Test subtraction operation.
        """
        inputs = ["5", "3", "-"]
        output = self.run_exercise(inputs)
        expected_output = "2.0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
