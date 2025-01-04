---
title: 102. Binary Tree Level Order Traversal
draft: false
tags: 
  - leetcode-medium
  - tree
  - breadth-first-search
  - binary-tree
date: 2020-12-18
---

[Problem Link](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## Description

---
<p>Given the <code>root</code> of a binary tree, return <em>the level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[9,20],[15,7]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1]
<strong>Output:</strong> [[1]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 2000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


## Solution

---
### Python3
``` py title='binary-tree-level-order-traversal'
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
### C++
``` cpp title='binary-tree-level-order-traversal'
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

