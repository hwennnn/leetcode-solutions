---
id: pascals-triangle
title: Pascal's Triangle
description: Problem Description and Solution for Pascal's Triangle
sidebar_label: 118. Pascal's Triangle
sidebar_position: 118
---

# [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/)

```py title=pascals-triangle.py
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = [[1] * (i + 1) for i in range(numRows)]
        
        for row in range(2, numRows):
            for j in range(1, len(A[row]) - 1):
                A[row][j] = A[row - 1][j - 1] + A[row - 1][j]
        
        return A
```

```java title=pascals-triangle.java
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> pre = null;
        for (int i = 1; i <= numRows; i++) {
            ArrayList<Integer> save = new ArrayList<>();
            for (int j = 1; j <= i; j++)
                if (j == 1 || j == i) save.add(1);
                else save.add(pre.get(j-1) + pre.get(j-2));
            result.add(save);
            pre = save;
        }
        return result;
    }
}
```


