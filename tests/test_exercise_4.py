import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise4(CustomTestCase):

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

    def test_initial_level(self):
        """
        Grade 1 is initial level.
        """
        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "initial level"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_average_level(self):
        """
        Grade 5 is average level.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "average level"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_sufficient_level(self):
        """
        Grade 8 is sufficient level.
        """
        inputs = ["8"]
        output = self.run_exercise(inputs)
        expected_output = "sufficient level"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_high_level(self):
        """
        Grade 11 is high level.
        """
        inputs = ["11"]
        output = self.run_exercise(inputs)
        expected_output = "high level"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_level_absent(self):
        """
        Grade 13 is level absent.
        """
        inputs = ["13"]
        output = self.run_exercise(inputs)
        expected_output = "level is absent"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
