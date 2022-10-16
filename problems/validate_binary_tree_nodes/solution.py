class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        inDegree = [0] * n
        def countNodes(node):
            if node == -1: return 0
            
            return 1 + countNodes(leftChild[node]) + countNodes(rightChild[node])
        
        for i, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                if inDegree[left] == 1: return False
                inDegree[left] += 1
            
            if right != -1:
                if inDegree[right] == 1: return False
                inDegree[right] += 1
        
        root = -1
        for i in range(n):
            if inDegree[i] == 0:
                if root == -1:
                    root = i
                else:
                    return False
        
        return root != -1 and countNodes(root) == n