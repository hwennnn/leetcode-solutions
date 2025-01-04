---
title: 1524. Number of Sub-arrays With Odd Sum
draft: false
tags: 
  - leetcode-medium
  - array
  - math
  - dynamic-programming
  - prefix-sum
date: 2020-08-26
---

[Problem Link](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

## Description

---
<p>Given an array of integers <code>arr</code>, return <em>the number of subarrays with an <strong>odd</strong> sum</em>.</p>

<p>Since the answer can be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,3,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,4,6]
<strong>Output:</strong> 0
<strong>Explanation:</strong> All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4,5,6,7]
<strong>Output:</strong> 16
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
</ul>


## Solution

---
### Python
``` py title='number-of-sub-arrays-with-odd-sum'
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        odd = even = res = 0
        M = 1000000007
        
        for num in arr:
            if num & 1:
                odd, even = even+1, odd
            else:
                odd, even = odd, even+1
                
            res += odd
        
        return res%M
        
```
### C++
``` cpp title='number-of-sub-arrays-with-odd-sum'
class Solution {
public:
    int numOfSubarrays(vector<int>& A) {
        int cur = 0, odd = 0, even = 1, mod = (int)1e9 + 7, res = 0;
        for (int a: A) {
            cur += a;
            if (cur%2){
                res = (res+even)%mod;
                odd++;
            }else{
                res = (res+odd)%mod;
                even++;
            }
        }
        return res;
    }
        
};
```
