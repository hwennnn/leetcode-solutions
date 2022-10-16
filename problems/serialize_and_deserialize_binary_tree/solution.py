# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def go(node):
            if not node:
                A.append('#')
            else:
                A.append(str(node.val))
                go(node.left)
                go(node.right)

        A = []
        go(root)
        return " ".join(A)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def go():
            val = next(A)
            if val == '#': return None
            
            node = TreeNode(int(val))
            node.left = go()
            node.right = go()
            
            return node

        A = iter(data.split(' '))
        return go()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))