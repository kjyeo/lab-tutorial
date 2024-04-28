import sys

# append the path of the
# parent directory
sys.path.append("..")

# import method from sibling module
from source.calculator import button_click, clear_display, backspace, toggle_sign, operate, get_entry

# import Python unittest
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        clear_display()

    def tearDown(self):
        clear_display()

    def test_button_click(self):
        # Test button click functionality
        # Add your test cases here

        # initialize
        clear_display()

        # positive test cases
        # Number 0..9 button press
        button_click('12')
        self.assertEqual(get_entry(), '12')

        # negative test cases
        # ...


    def test_clear_display(self):
        # Test clear display functionality
        # Add your test cases here

        clear_display()
        self.assertEqual(get_entry(), '')


    def test_backspace(self):
        # Test backspace functionality
        # Add your test cases here

        # initialize
        clear_display()
        
        # perform backspace when entry is empty
        backspace()
        self.assertNotEqual(get_entry(), 'Error')

        # perform backspace when entry contains numbers
        button_click('12')
        backspace()
        self.assertEqual(get_entry(), '1')

        # perform backspace resulting in entry is empty
        backspace()
        self.assertEqual(get_entry(), '')


    def test_toggle_sign(self):
        # Test toggle sign functionality
        # Add your test cases here

        # perform negate when entry is empty
        clear_display()
        toggle_sign()
        self.assertEqual(get_entry(), '-')

        # perform negate when entry contains a number
        clear_display()
        button_click('12')
        toggle_sign()
        self.assertEqual(get_entry(), '-12')

        toggle_sign()
        self.assertEqual(get_entry(), '12')

    def test_operate(self):
        # Test arithmetic operation functionality
        # Add your test cases here

        # addition of two positive numbers
        # addition of positive number to negative number
        # addition of two negative numbers

        # subtract a positive number from another positive number
        # subtract a positive number from a negative number
        # subtract a negative number from a negative number

        # multiply two positive numbers
        clear_display()
        button_click('8*2')
        operate()
        self.assertEqual(get_entry(), '16')

        # multiply positive number with negative number
        # multiply two negative numbers

        # divide two positive numbers
        # divide postive number with negative number
        # divide two negative numbers

        # divide by zero error

if __name__ == '__main__':
    unittest.main()
