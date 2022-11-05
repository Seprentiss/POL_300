import unittest
from gradescope_utils.autograder_utils.decorators import weight
import lists


class MyTestCase(unittest.TestCase):
    @weight(20)
    def test_accessing_data(self):
        output_1 = lists.access_list()
        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, "Luke")
        self.assertTrue(output_1 == "Luke", msg=error_1)

    @weight(60)
    def test_adding_data_at_index(self):
        correct_output_1 = ["Sam", "Paul", "Dan", "Luke", "George"]
        correct_output_2 = [1, 2, 3, 4, 5, 6]

        output_2, output_1 = lists.add_to_list()

        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, correct_output_1)
        error_2 = 'Output was "{}" Should be "{}"'.format(output_2, correct_output_2)

        self.assertTrue(output_1 == correct_output_1, msg=error_1)
        self.assertTrue(output_2 == correct_output_2, msg=error_2)

    @weight(20)
    def test_remove(self):
        correct_output_1 = ["Sam", "Paul", "Luke"]

        output_1 = lists.remove_from_list()

        error_1 = 'Output was "{}" Should be "{}"'.format(output_1, correct_output_1)

        self.assertTrue(output_1 == correct_output_1, msg=error_1)


if __name__ == '__main__':
    unittest.main()
