---
id: length-of-longest-fibonacci-subsequence
title: Length of Longest Fibonacci Subsequence
description: Problem Description and Solution for Length of Longest Fibonacci Subsequence
sidebar_label: 873. Length of Longest Fibonacci Subsequence
sidebar_position: 873
---

# [873. Length of Longest Fibonacci Subsequence](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)

```cpp title=length-of-longest-fibonacci-subsequence.cpp
class Solution {
public:
   int lenLongestFibSubseq(vector<int>& A) {
        unordered_set<int> s(A.begin(), A.end());
        int res = 0;
        for (int i = 0; i < A.size(); i++){
            for (int j = i+1; j < A.size(); j++){
                int first = A[i], second = A[j], l = 2;
                
                while (s.count(first+second)){
                    second = first+second, first = second-first, ++l;
                    res = max(res, l);
                }
            }
        }
       
       return res > 2 ? res : 0;
    }
};


```


