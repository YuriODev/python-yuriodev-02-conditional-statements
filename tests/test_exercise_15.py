import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise15(CustomTestCase):

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

    def test_end_of_month_transition(self):
        """
        Test end-of-month transition.
        """
        inputs = ["31", "1", "2020"]
        output = self.run_exercise(inputs)
        expected_output = "1.2.2020"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_leap_year_feb_end(self):
        """
        Test February end in a leap year.
        """
        inputs = ["29", "2", "2020"]
        output = self.run_exercise(inputs)
        expected_output = "1.3.2020"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_end_of_year_transition(self):
        """
        Test end-of-year transition.
        """
        inputs = ["31", "12", "2020"]
        output = self.run_exercise(inputs)
        expected_output = "1.1.2021"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
