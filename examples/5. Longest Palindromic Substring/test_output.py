import unittest
from output import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_longestPalindrome(self):
        test_cases = [
            ("babad", "bab"),  # "bab" is also a valid output
            ("cbbd", "bb"),
            ("a", "a"),
            ("ac", "a"),
            ("", ""),
            ("racecar", "racecar"),
            ("abcdefg", "a"),
            ("abb", "bb"),
        ]

        for i, (input, expected) in enumerate(test_cases):
            with self.subTest(test=i):
                self.assertEqual(self.sol.longestPalindrome(input), expected)

if __name__ == "__main__":
    unittest.main()
