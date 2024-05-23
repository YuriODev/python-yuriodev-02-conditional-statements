import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise9(CustomTestCase):

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

    def test_sum_greater(self):
        """
        Sum of the first and last digits is greater than the second.
        """
        inputs = ["123"]
        output = self.run_exercise(inputs)
        expected_output = ">"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_sum_lesser(self):
        """
        Sum of the first and last digits is less than the second.
        """
        inputs = ["251"]
        output = self.run_exercise(inputs)
        expected_output = "<"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_sum_equal(self):
        """
        Sum of the first and last digits is equal to the second.
        """
        inputs = ["143"]
        output = self.run_exercise(inputs)
        expected_output = "="
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
