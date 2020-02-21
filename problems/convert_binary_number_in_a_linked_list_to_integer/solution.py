# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 
       