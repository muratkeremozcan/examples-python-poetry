import unittest

class TestWord(unittest.TestCase):
    # Fixture setup method
    def setUp(self):
        # Initialize the word banana here
        self.word = "banana"

    # Test method
    def test_the_word(self):
        # Add the tests here
				# Create three tests to check that B and y are not in the list, and b is.
        self.assertNotIn("B", self.word)
        self.assertNotIn("y", self.word)
        self.assertIn("b", self.word)
    
    # Fixture teardown method
    def tearDown(self):
        # Use del when you want to completely remove the attribute
        del self.word


############

def check_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

def create_data():
    return ['level', 'step', 'peep', 'toot']

class TestPalindrome(unittest.TestCase):
    def setUp(self):
        # Initialize data here
        self.data = create_data()
    
    def test_func(self):
        expected_result = [True, False, True, True]
        data_checked = list(map(check_palindrome, self.data))
        # Verify the checked data here
        self.assertEqual(data_checked, expected_result)

    def tearDown(self):
        # Use clear() when you want to empty a mutable collection (like a list) but keep the attribute
        self.data.clear()
