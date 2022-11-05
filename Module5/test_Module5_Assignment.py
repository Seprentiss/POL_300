import Module5_Assignment
from gradescope_utils.autograder_utils.decorators import weight,partial_credit,number
import unittest

class TestCases(unittest.TestCase):
    @weight(100)
    def test_dataframe(self):
        output_1 = Module5_Assignment.calculate(
            Module5_Assignment.create_csv_df(Module5_Assignment.path))
        correct = 1497.0
        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, correct)
        self.assertTrue(output_1 == correct, msg=error_1)


if __name__ == '__main__': unittest.main(argv=[''], exit=False)