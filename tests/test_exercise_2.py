import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise2(CustomTestCase):

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
    def test_infant(self):
        """
        Person is an infant.
        """
        inputs = ["1"]
        output = self.run_exercise(inputs)
        expected_output = "You are an infant."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_child(self):
        """
        Person is a child.
        """
        inputs = ["5"]
        output = self.run_exercise(inputs)
        expected_output = "You are a child."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_teenager(self):
        """
        Person is a teenager.
        """
        inputs = ["15"]
        output = self.run_exercise(inputs)
        expected_output = "You are a teenager."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_adult(self):
        """
        Person is an adult.
        """
        inputs = ["25"]
        output = self.run_exercise(inputs)
        expected_output = "You are an adult."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
