# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        A = []
        
        def go(node):
            nonlocal A
            
            if not node: return
            
            A.append(node.val)
            
            go(node.left)
            go(node.right)
        
        go(root)
        A.sort()
        
        N = len(A)
        res = []
        
        for x in queries:
            left = bisect_left(A, x)
            right = bisect_right(A, x) - 1
            
            mmin = mmax = -1
            
            if 0 <= left < N:
                mmin = A[left]
            
            if 0 <= right < N:
                mmax = A[right]
            
            res.append([mmax, mmin])
        
        return res