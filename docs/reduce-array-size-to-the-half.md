---
id: reduce-array-size-to-the-half
title: Reduce Array Size to The Half
description: Problem Description and Solution for Reduce Array Size to The Half
sidebar_label: 1338. Reduce Array Size to The Half
sidebar_position: 1338
---

# [1338. Reduce Array Size to The Half](https://leetcode.com/problems/reduce-array-size-to-the-half/)

```py title=reduce-array-size-to-the-half.py
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        A = sorted(counter.values())
        curr = n
        res = 0
        
        while A and curr > n // 2:
            curr -= A.pop() 
            res += 1
        
        return res
```

```cpp title=reduce-array-size-to-the-half.cpp
class Solution {
public:
    int minSetSize(vector<int>& arr) {
    unordered_map<int, int> m;
    multiset<int, greater <int>> s;        
    for (auto n : arr) ++m[n];
    for (auto &p : m) s.insert(p.second);
    int res = 0, cnt = 0;
    for (auto it = begin(s); cnt * 2 < arr.size(); ++it) {
        ++res;
        cnt += *it;
    }
    return res;
}
};
```


