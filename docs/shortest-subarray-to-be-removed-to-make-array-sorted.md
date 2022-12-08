---
id: shortest-subarray-to-be-removed-to-make-array-sorted
title: Shortest Subarray to be Removed to Make Array Sorted
description: Problem Description and Solution for Shortest Subarray to be Removed to Make Array Sorted
sidebar_label: 1574. Shortest Subarray to be Removed to Make Array Sorted
sidebar_position: 1574
---

# [1574. Shortest Subarray to be Removed to Make Array Sorted](https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/)

```py title=shortest-subarray-to-be-removed-to-make-array-sorted.py
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        
        while left+1 < n and arr[left] <= arr[left+1]: left += 1
            
        if left + 1 == n: return 0
        
        right = n-1
        
        while left < right and arr[right] >= arr[right-1]: right -= 1
        
        res = min(n - left - 1, right)
        i = 0
        j = right
        while i <= left and j < n:
            if arr[j] >= arr[i]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
            
        
        return res 
```

```cpp title=shortest-subarray-to-be-removed-to-make-array-sorted.cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int n = arr.size();
        int left = 0;
        while (left+1 < n && arr[left+1] >= arr[left]) left++;
        if (left+1 == n) return 0;

        int right = n-1;
        while (right > left && arr[right-1] <= arr[right]) right--;

        int res = min(n - left - 1, right);
        int i = 0, j = right;

        while (i <= left && j < n){
            if (arr[j] >= arr[i]){
                res = min(res, j - i - 1);
                i++;
            }else{
                j++;
            }
        }

        return res;
    }
};
```


