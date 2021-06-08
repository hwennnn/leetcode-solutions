# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def helper(preStart, inStart, inEnd):
            if inStart > inEnd or preStart >= len(preorder): return None
            
            root = TreeNode(preorder[preStart])
            
            root_index = 0
            for i in range(inStart, inEnd + 1):
                if inorder[i] == root.val:
                    root_index = i
            
            root.left = helper(preStart + 1, inStart, root_index - 1)
            root.right = helper(preStart + root_index - inStart + 1, root_index + 1, inEnd)
            
            return root
        
        return helper(0, 0, len(inorder) - 1)