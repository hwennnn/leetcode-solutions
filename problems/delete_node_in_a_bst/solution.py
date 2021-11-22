# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def go(node, key):
            if not node: return None
            
            if node.val > key:
                node.left = go(node.left, key)
            elif node.val < key:
                node.right = go(node.right, key)
            else:
                if not node.left:
                    return node.right
                
                if not node.right:
                    return node.left
                
                successor = node.left
                while successor.right:
                    successor = successor.right
                
                node.val = successor.val
                node.left = go(node.left, node.val)
                
            return node
                
        return go(root, key)