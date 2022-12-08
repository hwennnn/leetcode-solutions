---
id: 3sum-with-multiplicity
title: 3Sum With Multiplicity
description: Problem Description and Solution for 3Sum With Multiplicity
sidebar_label: 923. 3Sum With Multiplicity
sidebar_position: 923
---

# [923. 3Sum With Multiplicity](https://leetcode.com/problems/3sum-with-multiplicity/)

```py title=3sum-with-multiplicity.py
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        n = len(arr)
        count = Counter()
        M = 10 ** 9 + 7
        res = 0
        
        for i in range(n):
            res = (res + count[target - arr[i]]) % M
            
            for j in range(i):
                m = arr[i] + arr[j]
                
                count[m] += 1
        
        return res
        
```

```java title=3sum-with-multiplicity.java
class Solution {
    public int threeSumMulti(int[] A, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        int res = 0;
        int mod = 1000000007;
        for (int i = 0; i < A.length; i++) {
            res = (res + map.getOrDefault(target - A[i], 0)) % mod;
            
            for (int j = 0; j < i; j++) {
                int temp = A[i] + A[j];
                map.put(temp, map.getOrDefault(temp, 0) + 1);
            }
        }
        return res;
    }
}
```


