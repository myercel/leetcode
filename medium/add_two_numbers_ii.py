"""
Problem No. 445

You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [7,2,4,3], l2 = [5,6,4]
    Output: [7,8,0,7]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       # use a stack to reverse the order of digits
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        curr = None

        while stack1 or stack2 or carry:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0

            val = v1 + v2 + carry

            carry = val // 10
            node = ListNode(val%10)
            node.next = curr
            curr = node

        return curr
        
        """
        # could store the nodes in a hashmap
        # the pass for creating the hashmap can be the pass for creating the new linked list?
        carry = 0
        dummy = curr = ListNode()
        l1_hashmap = {}
        l2_hashmap = {}
        i = 0

        newl1 = currl1 = ListNode()
        newl2 = currl2 = ListNode()

        # store all nodes in hashmaps
        while l1 or l2:
            if l1:
                l1_hashmap[i] = l1
            if l2:
                l2_hashmap[i] = l2

            i += 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # create the reversed lst
        for j in range(i, -1, -1):
            if j in l1_hashmap:
                newl1.next = l1_hashmap[j]
            if j in l2_hashmap:
                newl2.next = l2_hashmap[j]

        l1 = currl1.next
        l2 = currl2.next

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            currsum = v1 + v2 + carry
            carry = currsum // 10
            currsum = currsum % 10

            curr.next = ListNode(currsum)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
        """