from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given a list of integers `nums` and an integer `target`,
        returns the indices of the two numbers in `nums` that add up to the `target`.
        The function assumes that there is exactly one solution, and each element can be used only once.
        The function works efficiently with a time complexity of O(n).

        Parameters:
        nums (List[int]): A list of integers where the length is between 2 and 10^4.
                        Each element is an integer between -10^9 and 10^9.
        target (int): An integer between -10^9 and 10^9.

        Returns:
        List[int]: The indices of the two numbers in `nums` that add up to the `target`.
        """

        # Create a dictionary to store the numbers and their indices
        num_dict = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number with respect to the target
            complement = target - num

            # If the complement is found in the dictionary, return its index and the current index
            if complement in num_dict:
                return [num_dict[complement], i]

            # Otherwise, store the current number and its index in the dictionary
            num_dict[num] = i

        # If no solution is found (which will not happen according to the assumptions), return an empty list
        return []
