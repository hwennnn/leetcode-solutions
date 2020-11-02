# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
            
        ans = curr = ListNode(None)
        res.sort()
        
        for v in res:
            tmp = ListNode(v)
            if not curr:
                curr = tmp
            else:
                curr.next = tmp
            
            curr = curr.next
                
        
        
        return ans.next