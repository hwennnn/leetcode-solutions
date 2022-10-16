# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if not head: return True
        
        if not root: return False
        
        def go(node, ll, curr):
            if not curr: return True
            
            if not node: return False
            
            if node.val == curr.val:
                curr = curr.next
            elif node.val == ll.val:
                curr = ll.next
            else:
                return False
            
            return go(node.left, ll, curr) or go(node.right, ll, curr)
            
        
        return go(root, head, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)