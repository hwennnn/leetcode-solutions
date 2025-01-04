---
title: 111. Minimum Depth of Binary Tree
draft: false
tags: 
  - leetcode-easy
  - tree
  - depth-first-search
  - breadth-first-search
  - binary-tree
date: 2023-07-10
---

[Problem Link](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

## Description

---
<p>Given a binary tree, find its minimum depth.</p>

<p>The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.</p>

<p><strong>Note:</strong>&nbsp;A leaf is a node with no children.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [2,null,3,null,4,null,5,null,6]
<strong>Output:</strong> 5
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 10<sup>5</sup>]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
</ul>


## Solution

---
### Python3
``` py title='minimum-depth-of-binary-tree'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = collections.deque([[root,1]])
        
        while q:
            node, level = q.popleft()
            
            if node:
                if not node.left and not node.right:
                    return level
                
                for n in (node.left,node.right):
                    if n:
                        q.append([n, level + 1])
```

