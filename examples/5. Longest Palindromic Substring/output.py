# Here's a Python solution that expands around the center for each character and between each pair of characters in the string. 

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Find the longest palindromic substring in a given string.
        
        Parameters:
        s: str: Input string

        Returns:
        str: Longest palindromic substring
        """
        # If input string is empty or has length 1, return the string itself
        if len(s) < 2:
            return s

        # Initialize start and end pointers
        start = end = 0

        # Function to expand around the center
        def expand_around_center(s: str, left: int, right: int) -> tuple:
            # Expand as long as the characters are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the start and end indices of the palindrome
            return left + 1, right - 1

        # Iterate over each character and each pair of characters
        for i in range(len(s)):
            # Find a palindrome centered around i
            left1, right1 = expand_around_center(s, i, i)
            # Find a palindrome centered around i and i+1
            left2, right2 = expand_around_center(s, i, i + 1)
            # Compare the lengths of the two palindromes
            if right1 - left1 > right2 - left2:
                if right1 - left1 > end - start:
                    start, end = left1, right1
            else:
                if right2 - left2 > end - start:
                    start, end = left2, right2

        # Return the longest palindromic substring
        return s[start:end + 1]
  
# AutoPy - by Isaiah Bjorklund