# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def go(preStart, inStart, inEnd):
            if inStart > inEnd or preStart >= len(preorder): return None
            
            root = TreeNode(preorder[preStart])
            
            rootIndex = 0
            for index in range(inStart, inEnd + 1):
                if inorder[index] == root.val:
                    rootIndex = index
            
            root.left = go(preStart + 1, inStart, rootIndex - 1)
            root.right = go(preStart + rootIndex - inStart + 1, rootIndex + 1, inEnd)
            
            return root
        
        return go(0, 0, len(inorder) - 1)