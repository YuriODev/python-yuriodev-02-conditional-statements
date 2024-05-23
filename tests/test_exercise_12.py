import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise12(CustomTestCase):

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

    def test_replace_even_digits(self):
        """
        Even digits are replaced by '*'.
        """
        inputs = ["2468"]
        output = self.run_exercise(inputs)
        expected_output = "****"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_no_even_digits(self):
        """
        No even digits to replace.
        """
        inputs = ["1357"]
        output = self.run_exercise(inputs)
        expected_output = "1357"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
