import unittest
from output import two_sum

class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        # Test with positive numbers
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

        # Test with negative numbers
        nums = [-3, 4, 3, 90]
        target = 0
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 2])

        # Test with zeros
        nums = [0, 4, 3, 0]
        target = 0
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 3])

        # Test with large numbers
        nums = [1000000000, -1000000000]
        target = 0
        result = two_sum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_no_solution(self):
        # Test with no solution
        nums = [1, 2, 3, 4]
        target = 10
        result = two_sum(nums, target)
        self.assertEqual(result, [])

    def test_two_sum_single_solution(self):
        # Test with single solution
        nums = [1, 2, 3, 4]
        target = 7
        result = two_sum(nums, target)
        self.assertEqual(result, [2, 3])

if __name__ == "__main__":
    unittest.main()
