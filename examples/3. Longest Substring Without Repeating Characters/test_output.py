import unittest
from output import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_length_of_longest_substring(self):
        # Testing with an empty string
        self.assertEqual(self.solution.length_of_longest_substring(''), 0)

        # Testing with a string of one unique character
        self.assertEqual(self.solution.length_of_longest_substring('a'), 1)

        # Testing with a string of one repeating character
        self.assertEqual(self.solution.length_of_longest_substring('aaaaaaa'), 1)

        # Testing with a string of unique characters
        self.assertEqual(self.solution.length_of_longest_substring('abcdefg'), 7)

        # Testing with a string of repeating and unique characters
        self.assertEqual(self.solution.length_of_longest_substring('abcabcbb'), 3)

        # Testing with a string of repeating and unique characters
        self.assertEqual(self.solution.length_of_longest_substring('pwwkew'), 3)

        # Testing with a string where the longest substring without repeating characters is at the end
        self.assertEqual(self.solution.length_of_longest_substring('aabbccabcde'), 5)

        # Testing with a string where the longest substring without repeating characters is at the start
        self.assertEqual(self.solution.length_of_longest_substring('abcdeaabbcc'), 5)

        # Testing with a string where the longest substring without repeating characters is in the middle
        self.assertEqual(self.solution.length_of_longest_substring('aabbabcdecc'), 5)

if __name__ == "__main__":
    unittest.main()
