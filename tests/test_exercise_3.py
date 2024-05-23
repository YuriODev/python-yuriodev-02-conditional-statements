import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise3(CustomTestCase):

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

    def test_green(self):
        """
        Number 0 is green.
        """
        inputs = ["0\n"]
        output = self.run_exercise(inputs)
        expected_output = "Green"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_black(self):
        """
        Number 24 is black.
        """
        inputs = ["24\n"]
        output = self.run_exercise(inputs)
        expected_output = "Black"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_red(self):
        """
        Number 23 is red.
        """
        inputs = ["23\n"]
        output = self.run_exercise(inputs)
        expected_output = "Red"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_bet_not_play(self):
        """
        Number 37 will not play.
        """
        inputs = ["37\n"]
        output = self.run_exercise(inputs)
        expected_output = "The bet will not play!"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
