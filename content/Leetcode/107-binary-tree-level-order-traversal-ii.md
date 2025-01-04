---
title: 107. Binary Tree Level Order Traversal II
draft: false
tags: 
  - leetcode-medium
  - tree
  - breadth-first-search
  - binary-tree
date: 2020-10-22
---

[Problem Link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

## Description

---
<p>Given the <code>root</code> of a binary tree, return <em>the bottom-up level order traversal of its nodes&#39; values</em>. (i.e., from left to right, level by level from leaf to root).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[15,7],[9,20],[3]]
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
### Python
``` py title='binary-tree-level-order-traversal-ii'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        q, res = collections.deque([(root, 0)]), []
        
        while q:
            node, lvl = q.popleft()
            
            if node:
                if len(res) < lvl + 1:
                    res.insert(0, [])
                res[-(lvl+1)].append(node.val)
                for i in (node.left,node.right):
                    if i:
                        q.append([i, lvl+1])
                
        return res
```

