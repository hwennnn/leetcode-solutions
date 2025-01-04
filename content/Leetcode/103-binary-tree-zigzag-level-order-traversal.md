---
title: 103. Binary Tree Zigzag Level Order Traversal
draft: false
tags: 
  - leetcode-medium
  - tree
  - breadth-first-search
  - binary-tree
date: 2023-02-19
---

[Problem Link](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

## Description

---
<p>Given the <code>root</code> of a binary tree, return <em>the zigzag level order traversal of its nodes&#39; values</em>. (i.e., from left to right, then right to left for the next level and alternate between).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[3],[20,9],[15,7]]
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
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


## Solution

---
### Python
``` py title='binary-tree-zigzag-level-order-traversal'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        r = 0
        queue = collections.deque([root])
        
        while queue:
            l = []
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                l.append(node.val)
                
                for leaf in (node.left, node.right):
                    if leaf:
                        queue.append(leaf)
            
            if r: l.reverse()
            res.append(l)
            r ^= 1
        
        return res
```

