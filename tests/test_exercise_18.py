import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise18(CustomTestCase):

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

    def test_remember_name_yes_ex_yes_drunk_yes_rekindle(self):
        """
        Remember name: Yes, Ex: Yes, Drunk: Yes, Rekindle: Yes
        """
        inputs = ['yes', 'yes', 'yes', 'yes']
        output = self.run_exercise(inputs)
        expected_output = "Say hi."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_remember_name_yes_ex_yes_drunk_no(self):
        """
        Remember name: Yes, Ex: Yes, Drunk: Yes, Rekindle: No
        """
        inputs = ['yes', 'yes', 'yes', 'no']
        output = self.run_exercise(inputs)
        expected_output = "Don't say hi."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_remember_name_yes_ex_no_friend_ex_yes(self):
        """
        Remember name: Yes, Ex: No, Friend: Yes
        """
        inputs = ['yes', 'no', 'yes']
        output = self.run_exercise(inputs)
        expected_output = "Don't say hi."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_remember_name_yes_ex_no_friend_ex_no_enemy_no_convertible_yes(self):
        """
        Remember name: Yes, Ex: No, Friend: No, Enemy: No, Convertible: Yes
        """
        inputs = ['yes', 'no', 'no', 'no', 'yes']
        output = self.run_exercise(inputs)
        expected_output = "Don't say hi."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_remember_name_no_time_to_flee_yes(self):
        """
        Remember name: No, Time to flee: Yes
        """
        inputs = ['no', 'yes']
        output = self.run_exercise(inputs)
        expected_output = "Run for it."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_remember_name_no_time_to_flee_no_pretend_call_yes(self):
        """
        Remember name: No, Time to flee: No, Pretend call: Yes
        """
        inputs = ['no', 'no', 'yes']
        output = self.run_exercise(inputs)
        expected_output = "Hello, doctor. What are my test results?"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
