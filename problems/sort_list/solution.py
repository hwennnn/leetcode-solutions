# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        def merge(head1, head2):
            curr = res = ListNode(-1)
            
            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    curr.next = ListNode(head2.val)
                    head2 = head2.next
                
                curr = curr.next
            
            curr.next = head1 or head2
            
            return res.next
        
        pre, slow, fast = None, head, head
        
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        
        pre.next = None
        
        return merge(self.sortList(head), self.sortList(slow))