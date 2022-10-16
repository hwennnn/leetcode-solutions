# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        last = None
        
        for x in nums:
            while stack and stack[-1].val < x:
                last = stack.pop()        
            
            node = TreeNode(x)
            
            if stack:
                stack[-1].right = node
            
            if last:
                node.left = last
                
            
            stack.append(node)
            last = None
        
        return stack[0]