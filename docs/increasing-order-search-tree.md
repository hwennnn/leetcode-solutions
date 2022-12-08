---
id: increasing-order-search-tree
title: Increasing Order Search Tree
description: Problem Description and Solution for Increasing Order Search Tree
sidebar_label: 897. Increasing Order Search Tree
sidebar_position: 897
---

# [897. Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)

```py title=increasing-order-search-tree.py
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
```

```cpp title=increasing-order-search-tree.cpp
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
    TreeNode* increasingBST(TreeNode* root, TreeNode* tail = NULL) {
        if (!root) return tail;
        TreeNode* res = increasingBST(root->left, root);
        root->left = NULL;
        root->right = increasingBST(root->right, tail);
        return res;
    }
};
```


