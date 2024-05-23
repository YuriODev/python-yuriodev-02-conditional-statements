import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise10(CustomTestCase):

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

    def test_right_angled_triangle(self):
        """
        Triangle is right-angled.
        """
        inputs = ["0", "0", "0", "2", "4", "0"]
        output = self.run_exercise(inputs)
        expected_output = "Yes"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_not_right_angled_triangle(self):
        """
        Triangle is not right-angled.
        """
        inputs = ["0", "0", "0", "0", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "No"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
