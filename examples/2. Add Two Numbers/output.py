# AutoPy - by Isaiah Bjorklund

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This function takes in two linked lists which represent two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        It adds the two numbers and returns the sum as a linked list.

        :param l1: First input linked list
        :param l2: Second input linked list
        :return: A linked list which is the sum of the input linked lists
        """
 
        # initializing dummy node
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # variable to handle carry over, if any

        # while loop to iterate through the lists
        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            curr.next = ListNode(out)
            curr = curr.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return dummy.next  # return the next of dummy node, which is the head of our resultant list
