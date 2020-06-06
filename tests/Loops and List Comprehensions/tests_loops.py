import unittest
from App.Loops_and_List_Comprehensions.loops import *

class LoopsTests(unittest.TestCase):

    def test_has_lucky_number(self):
        """Test for function 'has_lucky_number'"""
        self.assertTrue(has_lucky_number([1, 2, 7, 4]))
        self.assertIs(has_lucky_number([1, 2, 2, 4]), False)

    def test_elementwise_greater_than(self):
        """Test for function 'elementwise_greater_than'"""
        self.assertEqual(elementwise_greater_than([1, 2, 2, 4], 1), [False, True, True, True])
        self.assertEqual(elementwise_greater_than([1, 2, 2, 4], 2), [False, False, False, True])

    def test_elementwise_greater_than_two(self):
        """Test for function 'elementwise_greater_than_two'"""
        self.assertEqual(elementwise_greater_than_two([1, 2, 2, 4], 0), [True, True, True, True])
        self.assertEqual(elementwise_greater_than_two([0.35, 7.01, 22, 44], 7), [False, True, True, True])


    def test_menu_is_boring(self):
        """Test for funnction 'menu_is_boring'"""
        pass




if __name__ == '__main__':
    unittest.main()