# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = []
        prev = None
        curr = head
        index = 0
        
        while curr:
            index += 1
            if prev and curr.next:
                p, n = prev.val, curr.next.val
                if curr.val > p and curr.val > n or curr.val < p and curr.val < n:
                    res.append(index)
                
            prev = curr
            curr = curr.next
        
        if len(res) < 2: return [-1, -1]
        
        mmin = float('inf')
        for i in range(1, len(res)):
            mmin = min(mmin, res[i] - res[i - 1])
        
        return [mmin, max(res) - min(res)]