# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        n = len(lists)
        
        def mergeLists(start, end):
            if start == end: 
                return lists[start]
            elif start < end:
                mid = start + (end - start) // 2
                
                l1 = mergeLists(start, mid)
                l2 = mergeLists(mid + 1, end)
                
                return merge(l1, l2)
            else:
                return None
        
        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            
            res = curr = ListNode()
            
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                    
                curr = curr.next
            
            curr.next = l1 or l2
            
            return res.next
        
        return mergeLists(0, n - 1)