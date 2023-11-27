# We will use Python's built-in bisect module to find the median of two sorted arrays.
# To do this, we will first merge the two sorted arrays using the merge function from heapq module.
# Then we will find the middle element(s) depending on the length of the merged array.

from typing import List
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays
        
        :param nums1: First sorted array
        :type nums1: List[int]
        :param nums2: Second sorted array
        :type nums2: List[int]
        
        :return: Median of the two arrays
        :rtype: float
        """
        # Merge the two sorted arrays
        merged = list(heapq.merge(nums1, nums2))
        
        # Calculate the length of the merged array
        length = len(merged)
        
        # If the length is even, the median is the average of the two middle elements
        if length % 2 == 0:
            return (merged[length // 2] + merged[length // 2 - 1]) / 2.0
        
        # If the length is odd, the median is the middle element
        return float(merged[length // 2])