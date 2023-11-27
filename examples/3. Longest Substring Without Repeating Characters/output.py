class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        """
        Given a string s, this function finds the length of the longest substring 
        without repeating characters.

        :param s: input string
        :return: length of the longest substring without repeating characters
        """

        # Initialize a dictionary to store visited characters and their index
        visited = {}
        max_length = start = 0

        for index, char in enumerate(s):
            # If the character is already in the visited dictionary and its 
            # index is greater or equal than the current start index
            if char in visited and start <= visited[char]:
                # Update the start index
                start = visited[char] + 1
            else:
                # Update the max length
                max_length = max(max_length, index - start + 1)

            # Update the visited character's index
            visited[char] = index
        
        return max_length
