# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nums = []
        
        for l in lists:
            curr = l
            while curr:
                nums.append(curr.val)
                curr = curr.next
                
        nums.sort()
        
        curr = res = ListNode()
        for x in nums:
            node = ListNode(x)
            curr.next = node
            curr = curr.next
        
        return res.next