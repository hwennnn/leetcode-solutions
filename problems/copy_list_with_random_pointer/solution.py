"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        res = collections.defaultdict(lambda: Node(0))
        res[None] = None

        curr = head
        while curr:
            res[curr].val = curr.val
            res[curr].next = res[curr.next]
            res[curr].random = res[curr.random]
            curr = curr.next

        return res[head]