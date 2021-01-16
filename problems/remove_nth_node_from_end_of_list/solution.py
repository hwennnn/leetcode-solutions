# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        res = []
        
        ans = head
        while head:
            res.append(head)
            head = head.next
            
        n = len(res)
        if n - k - 1 < 0: return ans.next
        
        res[n-k-1].next = res[n-k+1] if (n-k+1) < n else None

        return ans
            