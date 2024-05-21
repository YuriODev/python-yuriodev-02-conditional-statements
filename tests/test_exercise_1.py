import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise1(CustomTestCase):

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

    def test_older_alex(self):
        """Alex is older than Tatyana."""
        inputs = ['30', '25']
        output = self.run_exercise(inputs)
        expected_output = "Alex is the eldest."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_older_tatyana(self):
        """Tatyana is older than Alex."""
        inputs = ['22', '30']
        output = self.run_exercise(inputs)
        expected_output = "Tatyana is the eldest."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_same_age(self):
        """Alex and Tatyana are of the same age."""
        inputs = ['25', '25']
        output = self.run_exercise(inputs)
        expected_output = "Alex and Tatyana are of the same age."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
