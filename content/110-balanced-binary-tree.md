---
title: 110. Balanced Binary Tree
draft: false
tags: 
  - leetcode-easy
  - tree
  - depth-first-search
  - binary-tree
date: 2020-12-22
---

[Problem Link](https://leetcode.com/problems/balanced-binary-tree/)

## Description

---
<p>Given a binary tree, determine if it is <span data-keyword="height-balanced"><strong>height-balanced</strong></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [1,2,2,3,3,null,null,4,4]
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> root = []
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-10<sup>4</sup> &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

---
### Python3
``` py title='balanced-binary-tree'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            l, r = go(node.left), go(node.right)
            
            if abs(l - r) > 1:
                res = False
            
            return 1 + max(l, r)
        
        go(root)
        
        return res
```
### C++
``` cpp title='balanced-binary-tree'
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
    int dfs(TreeNode* root){
        if (root == nullptr) return 0;
        
        int left = dfs(root->left);
        int right = dfs(root->right);
        
        if (left == -1 || right == -1 || abs(left-right) > 1) return -1;
        
        return 1 + max(left, right);
    }
    
    bool isBalanced(TreeNode* root) {
        return dfs(root) != -1;
    }
};
```

