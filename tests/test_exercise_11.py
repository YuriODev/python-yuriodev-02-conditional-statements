import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise11(CustomTestCase):

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

    def test_leap_year(self):
        """
        Year is a leap year.
        """
        inputs = ["2020"]
        output = self.run_exercise(inputs)
        expected_output = "Leap year."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_leap_year_2(self):
        """
        Year is a leap year.
        """
        inputs = ["2000"]
        output = self.run_exercise(inputs)
        expected_output = "Leap year."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_leap_year_3(self):
        """
        Year is a leap year.
        """
        inputs = ["2016"]
        output = self.run_exercise(inputs)
        expected_output = "Leap year."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_not_leap_year(self):
        """
        Year is not a leap year.
        """
        inputs = ["2019"]
        output = self.run_exercise(inputs)
        expected_output = "Ordinary year."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
