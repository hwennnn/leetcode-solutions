---
id: sum-of-floored-pairs
title: Sum of Floored Pairs
description: Problem Description and Solution for Sum of Floored Pairs
sidebar_label: 1862. Sum of Floored Pairs
sidebar_position: 1862
---

# [1862. Sum of Floored Pairs](https://leetcode.com/problems/sum-of-floored-pairs/)

```py title=sum-of-floored-pairs.py
class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        M = 10 ** 9 + 7
        
        prefix = [0] * (max(nums) + 1)
        counter = collections.Counter(nums)
        
        for num, count in counter.items():
            for j in range(num, len(prefix), num):
                prefix[j] += count
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i - 1]
        
        return sum(prefix[num] for num in nums) % M
```

```cpp title=sum-of-floored-pairs.cpp
class Solution {
public:
    const int MAXN = 1e5 + 1, MOD = 1e9 + 7;
    int sumOfFlooredPairs(vector<int>& nums) {
        vector<long> freq(2*MAXN+1);        
        long mx = 0, sum = 0;
        for(auto num : nums) ++freq[num], mx = max((int)mx, num);  // counting frequency of each element in nums
        for(int i = 1; i <= 2*MAXN; ++i) freq[i] += freq[i - 1];   // building prefix sum array of freq. Now freq[i] will hold the frequency of numbers less than or equal to i
        // Each num will be assumed in the denominator as floor(nums[i] / num) and 
        // using freq array, we can calculate the number of terms contributing 1, 2, 3... to the sum each.
        for(auto num : nums) { 
            long l = num, r = 2 * num - 1, divResult = 1;
            while(l <= mx) {                
                sum = (sum + divResult * (freq[r] - freq[l - 1])) % MOD;
                l += num, r += num;
                ++divResult;
            }
        }
        return sum;
    }
};
```


