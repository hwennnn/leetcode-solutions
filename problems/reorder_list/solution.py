# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        if fast.next:
            fast = fast.next
            
        # reverse the second half of the list
        prev = slow
        curr = slow.next
        prev.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        # turn the list into zigzag manner
        trav = head
        while fast.next:
            tmp1 = trav.next
            tmp2 = fast.next
            trav.next = fast
            fast.next = tmp1
            trav = tmp1
            fast = tmp2
        