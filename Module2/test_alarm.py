import alarm
from gradescope_utils.autograder_utils.decorators import weight,partial_credit,number
import unittest

class TestCases(unittest.TestCase):
    @weight(50)
    def test_weekday(self):
        error = "Incorrect Time!"
        self.assertTrue(alarm.alarm(1,False) == "7:00",msg=error)
        self.assertTrue(alarm.alarm(4, True) == "10:00", msg=error)

    @weight(50)
    def test_weekend(self):
        error = "Incorrect Time!"

        self.assertTrue(alarm.alarm(6, False) == "10:00", msg=error)
        self.assertTrue(alarm.alarm(7, True) == "off", msg=error)



if __name__ == '__main__': unittest.main(argv=[''], exit=False)