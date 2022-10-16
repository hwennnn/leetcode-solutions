# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def generate(start, end):
            res = []
            
            if start > end:
                res.append(None)
            
            for index in range(start, end + 1):
                left = generate(start, index - 1)
                right = generate(index + 1, end)
                
                for l in left:
                    for r in right:
                        node = TreeNode(index, l, r)
                        res.append(node)
            
            return res
        
        return generate(1, n)