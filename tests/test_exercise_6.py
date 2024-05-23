import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise6(CustomTestCase):

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

    def test_point_a_further(self):
        """
        Point A is further from the origin than B.
        """
        inputs = ["3", "4", "1", "2"]
        output = self.run_exercise(inputs)
        expected_output = "A is further from the origin."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_point_b_further(self):
        """
        Point B is further from the origin than A.
        """
        inputs = ["1", "1", "4", "5"]
        output = self.run_exercise(inputs)
        expected_output = "B is further from the origin."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_same_distance(self):
        """
        Points A and B are at the same distance from the origin.
        """
        inputs = ["3", "4", "-3", "-4"]
        output = self.run_exercise(inputs)
        expected_output = "A and B are at the same distance from the origin."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
