# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        
        deq = collections.deque([root])
        
        while deq:
            node = deq.popleft()
            
            arr.append(node.val)
            
            for n in (node.left, node.right):
                if n:
                    deq.append(n)
            
        arr.sort()
        
        head = curr = TreeNode(arr[0])
        
        for num in arr[1:]:
            c = TreeNode(num)
            curr.right = c
            curr = curr.right
        
        
        return head