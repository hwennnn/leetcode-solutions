---
id: ways-to-split-array-into-three-subarrays
title: Ways to Split Array Into Three Subarrays
description: Problem Description and Solution for Ways to Split Array Into Three Subarrays
sidebar_label: 1712. Ways to Split Array Into Three Subarrays
sidebar_position: 1712
---

# [1712. Ways to Split Array Into Three Subarrays](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/)

```py title=ways-to-split-array-into-three-subarrays.py
class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
            
        n = len(nums)
        M = 10 ** 9 + 7
        res = 0

        for i in range(1, n-1):
            mid = bisect_left(prefix, 2 * prefix[i])
            right = bisect_right(prefix, (prefix[-1] + prefix[i]) // 2)
            res += max(0, min(n,right) - max(i+1, mid))
        
        return res % M
```

```cpp title=ways-to-split-array-into-three-subarrays.cpp
class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        int M = 1e9 + 7;
        int n = nums.size();
        
        for (int i = 1; i < n; i++)
            nums[i] += nums[i-1];
        
        long long res = 0;
        for (int i = 0; i < n - 1; i++){
            int left = nums[i];
            int remaining = nums[n-1] - left;
            int max_mid = remaining / 2;
            
            int mid_start = lower_bound(nums.begin()+i+1, nums.end()-1, left * 2) - nums.begin();
            int right_start = upper_bound(nums.begin()+i+1, nums.end()-1, left + max_mid) - nums.begin();
            
            res += max(0, right_start - mid_start);
            res %= M;
        }
        
        return res % M;
    }
};
```

```java title=ways-to-split-array-into-three-subarrays.java
class Solution {
    public int waysToSplit(int[] nums) {

        int MOD = (int) (1e9 + 7);

        int N = nums.length;

        // prefix array
        int[] A = new int[N];
        A[0] = nums[0];
        for (int i = 1; i < N; ++i) A[i] = A[i - 1] + nums[i];

        int res = 0;
        for (int i = 1; i < N - 1; ++i) {

            int left = helper(A, A[i - 1], i, true);
            int right = helper(A, A[i - 1], i, false);

            if (left == -1 || right == -1) continue;  // none is satisfied

            res = (res + (right - left + 1) % MOD) % MOD;
        }

        return res;
    }

    private int helper(int[] A, int leftSum, int index, boolean searchLeft) {

        int N = A.length;
        int l = index, r = N - 2;
        int res = -1;

        while (l <= r) {

            int m = (r - l) / 2 + l;

            int midSum = A[m] - A[index - 1];
            int rightSum = A[N - 1] - A[m];

            if (leftSum <= midSum && midSum <= rightSum) {
                res = m;
                if (searchLeft) r = m - 1;
                else l = m + 1;
            } else if (leftSum > midSum) {  // shrink left
                l = m + 1;
            } else {  // shrink right
                r = m - 1;
            }
        }

        return res;
    }
}
```


