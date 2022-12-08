---
id: validate-binary-tree-nodes
title: Validate Binary Tree Nodes
description: Problem Description and Solution for Validate Binary Tree Nodes
sidebar_label: 1361. Validate Binary Tree Nodes
sidebar_position: 1361
---

# [1361. Validate Binary Tree Nodes](https://leetcode.com/problems/validate-binary-tree-nodes/)

```py title=validate-binary-tree-nodes.py
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
```

```cpp title=validate-binary-tree-nodes.cpp
class Solution {
public:
   int countNodes(vector<int> &l,vector<int> &r,int root)   // DFS from root to validate that all nodes are visited.
    {
        if(root==-1)
            return 0;
        return 1+countNodes(l,r,l[root])+countNodes(l,r,r[root]);
    }
    bool validateBinaryTreeNodes(int n, vector<int>& leftChild, vector<int>& rightChild) 
    {
        vector<int> inDegree(n,0);
        int root=-1;
        for(int i=0;i<leftChild.size();i++)
            if(leftChild[i]!=-1&&inDegree[leftChild[i]]++==1)  //If in-degree exceeds 1 return false.
                return false;
            else if(rightChild[i]!=-1&&inDegree[rightChild[i]]++==1)  //If in-degree exceeds 1 return false.
                return false;
        for(int i=0;i<leftChild.size();i++)    //Find root and also check for multiple roots.
            if(inDegree[i]==0)  //If in-degree = 0 and has children it's a root.
                if(root==-1)   //Store the root.
                    root=i;
                else    //We have multiple roots, return false
                    return false;
        if(root==-1)
            return false;
        return countNodes(leftChild,rightChild,root)==n;
    }
};
```


