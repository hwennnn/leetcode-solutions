---
id: maximum-length-of-subarray-with-positive-product
title: Maximum Length of Subarray With Positive Product
description: Problem Description and Solution for Maximum Length of Subarray With Positive Product
sidebar_label: 1567. Maximum Length of Subarray With Positive Product
sidebar_position: 1567
---

# [1567. Maximum Length of Subarray With Positive Product](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/)

```py title=maximum-length-of-subarray-with-positive-product.py
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res = negCount = 0
        zeroPos = negPos = -1
        
        for i, x in enumerate(nums):
            if x < 0:
                negCount += 1
                if negPos == -1:
                    negPos = i
            elif x == 0:
                negCount = 0
                zeroPos = i
                negPos = -1
            
            if negCount % 2 == 0:
                res = max(res, i - zeroPos)
            else:
                res = max(res, i - negPos)
        
        return res
```

```cpp title=maximum-length-of-subarray-with-positive-product.cpp
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int n = nums.size();
        int lastZero = -1;
        int firstNegative = -1;
        int res = 0;
        int neg = 0;
        
        for (int i = 0; i < n; i++){
            if (nums[i] < 0){
                 neg++;
                if (firstNegative == -1){
                    firstNegative = i;
                }
        
            }
            
            if (nums[i] == 0){
                neg = 0;
                firstNegative = -1;
                lastZero = i;
            }else{
                if (neg%2 == 0){
                    res = max(res, i - lastZero);
                }
                else{
                    res = max(res, i - firstNegative);
                }
            }
            
            
               
        }
        
        return res;
            
            
            
    }
};

```

```java title=maximum-length-of-subarray-with-positive-product.java
class Solution {
      public int getMaxLen(int[] nums) {
        // sum is used to count the number of negative numbers from zeroPosition to current index
        int firstNegative = -1, zeroPosition = -1, sum = 0, max = 0;
        for(int i = 0;i < nums.length; i++){
            if(nums[i] < 0){
                sum++;
				// we only need to know index of first negative number
                if(firstNegative == -1) firstNegative = i;
            }
			// if current number is 0, we can't use any element from index 0 to i anymore, so update zeroPosition, and reset sum and firstNegative. If it is a game, we should refresh the game when we meet 0. 
            if(nums[i] == 0){
                sum = 0;
                firstNegative = -1;
                zeroPosition = i;
            }
            else{
			    // consider index of zero
                if(sum%2 == 0) max = Math.max(i - zeroPosition, max);
				// consider index of first negative number
                else max = Math.max(i - firstNegative, max);   
            }
        }
        return max;
    }
}
```


