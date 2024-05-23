import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise17(CustomTestCase):

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

    def test_lucky_ticket_true(self):
        """
        Ticket is lucky.
        """
        inputs = ["123321"]
        output = self.run_exercise(inputs)
        expected_output = "Happy"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_lucky_ticket_false(self):
        """
        Ticket is not lucky.
        """
        inputs = ["123456"]
        output = self.run_exercise(inputs)
        expected_output = "Ordinary"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
