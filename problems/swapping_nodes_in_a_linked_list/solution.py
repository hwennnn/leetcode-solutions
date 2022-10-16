# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        res = []
        
        curr = head
        while curr:
            res.append(curr)
            curr = curr.next
        
        res[k-1].val, res[-k].val = res[-k].val, res[k-1].val
        
        return head