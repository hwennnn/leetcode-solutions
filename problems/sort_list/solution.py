# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        
        arr = []
        
        while head:
            arr.append(head.val)
            head = head.next
            
        arr.sort()
        res = node = ListNode()
        
        for i,v in enumerate(arr):
            tmp = node
            tmp.val = v
            if i != len(arr) - 1:
                tmp.next = ListNode()
            node = tmp
            node = node.next
        
        return res