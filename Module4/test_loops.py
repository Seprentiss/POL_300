import unittest
from gradescope_utils.autograder_utils.decorators import weight
import loops


class MyTestCase(unittest.TestCase):
    @weight(20)
    def test_for_loop(self):
        output_1 = loops.for_loop()
        correct = "0123456789"

        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, correct)
        self.assertTrue(output_1 == correct, msg=error_1)

    @weight(20)
    def test_while_loop(self):

        output_1 = loops.while_loop()

        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, 45)

        self.assertTrue(output_1 == 45, msg=error_1)

    @weight(60)
    def test_sum_evens_sub_odds(self):
        correct_output_1 = 3

        output_1 = loops.sum_evens_sub_odds()

        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, correct_output_1)

        self.assertTrue(output_1 == correct_output_1, msg=error_1)


if __name__ == '__main__':
    unittest.main()
