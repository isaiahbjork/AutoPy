import unittest
from output import ListNode, Solution

class TestSolution(unittest.TestCase):

    def create_linked_list(self, elements):
        """
        Helper method to create linked list from list of elements.
        """
        dummy_root = ListNode(0)
        ptr = dummy_root
        for number in elements:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummy_root.next
        return ptr

    def linked_list_to_list(self, node):
        """
        Helper method to convert linked list to list.
        """
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_addTwoNumbers(self):
        solution = Solution()
        
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        expected_output = [7, 0, 8]
        test_result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(test_result), expected_output)
        
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([0])
        expected_output = [0]
        test_result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(test_result), expected_output)

        l1 = self.create_linked_list([9,9,9,9,9,9,9])
        l2 = self.create_linked_list([9,9,9,9])
        expected_output = [8,9,9,9,0,0,0,1]
        test_result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(test_result), expected_output)

if __name__ == "__main__":
    unittest.main()
