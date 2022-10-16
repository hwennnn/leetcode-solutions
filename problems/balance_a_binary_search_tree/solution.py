# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def storeNodes(root, arr):
            if not root: return
            
            storeNodes(root.left,arr)
            arr.append(root.val)
            storeNodes(root.right,arr)
        
        def build(arr):
            if not arr: return None
            
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            
            return root

        arr = []
        storeNodes(root,arr)
        
        return build(arr)