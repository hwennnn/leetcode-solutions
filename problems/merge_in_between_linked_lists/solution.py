# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        res = head = curr = ListNode()
        curr.next = list1
        
        l = -1
        
        while curr:
            if l == a:
                head = curr.next

            if l == b:
                c = list2
                while c.next:
                    c = c.next
                curr = curr.next
                while curr:
                    c.next = curr
                    curr = curr.next
                    c = c.next

                break

            curr = curr.next
            l += 1
            
        l = -1
        temp = res
        while temp and l+1 != a:
            temp = temp.next
            l += 1
        
        temp.next = list2
        
        return res.next
