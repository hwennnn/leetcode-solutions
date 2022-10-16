# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        def depth(node):
            if not node: return 0
            
            return 1 + max(depth(node.left), depth(node.right))
        
        d = depth(root)
        res = 0
        q = collections.deque([(root, 1)])
        
        while q:
            node, depth = q.popleft()

            if depth == d: res += node.val
                
            for leaf in (node.left, node.right):
                if leaf:
                    q.append((leaf, depth + 1))
        
        return res
                
        