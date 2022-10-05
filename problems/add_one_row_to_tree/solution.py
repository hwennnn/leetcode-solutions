# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            
            return newRoot
        
        d = 1
        dq = deque([root])
        
        while dq:
            N = len(dq)
            
            for _ in range(N):
                node = dq.popleft()
                
                if d + 1 == depth:
                    oLeft = node.left
                    oRight = node.right
                    newLeftNode = TreeNode(val)
                    newLeftNode.left = oLeft
                    
                    newRightNode = TreeNode(val)
                    newRightNode.right = oRight
                    
                    node.left = newLeftNode
                    node.right = newRightNode
                    
                else:
                    for child in filter(None, (node.left, node.right)):
                        dq.append(child)
            
            if d + 1 == depth:
                break
                
            d += 1
        
        return root