# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.A = []
        self.n = 0
        
        curr = head
        while curr:
            self.A.append(curr.val)
            curr = curr.next
            self.n += 1

    def getRandom(self) -> int:
        n = random.randint(0, self.n - 1)
        
        return self.A[n]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()