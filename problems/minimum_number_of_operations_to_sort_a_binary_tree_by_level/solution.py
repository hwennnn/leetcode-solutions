# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        levels = []
        dq = deque([root])
        
        while dq:
            N = len(dq)
            curr = []
            
            for _ in range(N):
                node = dq.popleft()
                curr.append(node.val)
                
                for leaf in (node.left, node.right):
                    if leaf:
                        dq.append(leaf)
            
            levels.append(curr)

        for arr in levels:
            s = sorted(arr)
            t2 = {x: i for i, x in enumerate(arr)}
            
            for ti, tx in enumerate(s):
                if tx == arr[ti]: continue

                res += 1
                a, b = arr[ti], arr[t2[tx]]
                arr[ti], arr[t2[tx]] = arr[t2[tx]], arr[ti]
                t2[a], t2[b] = t2[tx], ti
        
        return res