import unittest
from .test_utils import CustomTestCase, CustomTestRunner


class TestExercise5(CustomTestCase):

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

    def test_two_distinct_roots(self):
        """
        Quadratic equation with two distinct real roots.
        """
        inputs = ["1", "-3", "2"]
        output = self.run_exercise(inputs)
        expected_output = "and"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_single_root(self):
        """
        Quadratic equation with a single real root (discriminant is zero).
        """
        inputs = ["1", "-2", "1"]
        output = self.run_exercise(inputs)
        self.assertTrue(any(x in output for x in ["1.0", "-1.0"]))  # Check for the presence of the root

    def test_no_real_roots(self):
        """
        Quadratic equation with no real roots (negative discriminant).
        """
        inputs = ["1", "2", "5"]
        output = self.run_exercise(inputs)
        expected_output = "No roots."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_linear_equation_one_root(self):
        """
        Linear equation with one root.
        """
        inputs = ["0", "2", "-4"]
        output = self.run_exercise(inputs)
        expected_output = "2.0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_invalid_linear_equation(self):
        """
        Invalid linear equation (b=0, c!=0).
        """
        inputs = ["0", "0", "3"]
        output = self.run_exercise(inputs)
        expected_output = "No roots."
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_linear_equation_c_zero(self):
        """
        Linear equation reduced to c=0 (b!=0).
        """
        inputs = ["0", "2", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_b_zero_c_nonzero_positive_roots(self):
        """
        Quadratic equation with b=0 and c!=0 leading to positive roots.
        """
        inputs = ["1", "0", "-9"]
        output = self.run_exercise(inputs)
        expected_output = "and"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_b_zero_c_zero_root(self):
        """
        Quadratic equation with b=0 and c=0.
        """
        inputs = ["1", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "0"
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)

    def test_all_zero_infinite_solutions(self):
        """
        All coefficients zero, theoretically infinite solutions.
        """
        inputs = ["0", "0", "0"]
        output = self.run_exercise(inputs)
        expected_output = "Infinite roots."  # Placeholder check
        self.assertInCustom(expected=expected_output,
                            actual=output, input_value=inputs)


if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())