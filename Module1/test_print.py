import hello
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
import unittest

class TestCases(unittest.TestCase):
    @weight(100)
    def test(self):
        student_name = hello.first_name
        output = hello.welcome(student_name)
        correct_output = "Welcome to POL 300, " + student_name + "!"
        error = 'Output was "{}" Should be "{}"'.format(output, correct_output)

        self.assertEqual(output, correct_output,msg=error)


if __name__ == '__main__': unittest.main(argv=[''], exit=False)