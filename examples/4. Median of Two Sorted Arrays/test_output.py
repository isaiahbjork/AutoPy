import unittest
from output import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        # Test arrays of even length
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6, 8]
        expected_result = 4.5
        actual_result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(actual_result, expected_result, "Failed on Test Case 1")

        # Test arrays of odd length
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        expected_result = 3.5
        actual_result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(actual_result, expected_result, "Failed on Test Case 2")

        # Test arrays with negative numbers
        nums1 = [-5, -3, -1]
        nums2 = [-4, -2, 0]
        expected_result = -2.5
        actual_result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(actual_result, expected_result, "Failed on Test Case 3")

        # Test arrays with single element
        nums1 = [1]
        nums2 = [2]
        expected_result = 1.5
        actual_result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(actual_result, expected_result, "Failed on Test Case 4")

        # Test arrays with single array is empty
        nums1 = []
        nums2 = [1, 2, 3, 4, 5]
        expected_result = 3.0
        actual_result = self.solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(actual_result, expected_result, "Failed on Test Case 5")

if __name__ == '__main__':
    unittest.main()
