"""
Problem No. 148

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # left lst
        left = head
        right = self.getmid(head)
        tmp = right.next
        right.next = None
        # right lst
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def getmid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next

        """
        nodes = {}
        dummy = curr = ListNode()

        # fill in the dictionary with val:node pairs
        while head:
            nodes[head.val] = head
            head = head.next
        
        keys = list(nodes.keys())
        keys.sort()

        for key in keys:
            curr.next = nodes[key]
            curr = curr.next
        
        return dummy.next
        """