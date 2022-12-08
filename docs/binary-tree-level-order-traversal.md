---
id: binary-tree-level-order-traversal
title: Binary Tree Level Order Traversal
description: Problem Description and Solution for Binary Tree Level Order Traversal
sidebar_label: 102. Binary Tree Level Order Traversal
sidebar_position: 102
---

# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```py title=binary-tree-level-order-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        res = []
        dq = deque([root])
        
        while dq:
            n = len(dq)
            curr = []
            
            for _ in range(n):
                node = dq.popleft()
                curr.append(node.val)
                
                for child in (node.left, node.right):
                    if child:
                        dq.append(child)
            
            res.append(curr)
        
        return res
```

```cpp title=binary-tree-level-order-traversal.cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> q; q.push(root);
        vector<vector<int>> res;
        
        if (root == nullptr) return res;
        
        while (q.size() > 0){
            vector<int> tmp;
            int length = q.size();
            
            while (length--){
                TreeNode* node = q.front();
                tmp.push_back(node->val);
                q.pop();
                
                if (node->left){
                    q.push(node->left);
                }
                
                if (node->right){
                    q.push(node->right);
                }
            }
            
            res.push_back(tmp);
        }
        
        return res;
    }
};
```


