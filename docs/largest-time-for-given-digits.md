---
id: largest-time-for-given-digits
title: Largest Time for Given Digits
description: Problem Description and Solution for Largest Time for Given Digits
sidebar_label: 949. Largest Time for Given Digits
sidebar_position: 949
---

# [949. Largest Time for Given Digits](https://leetcode.com/problems/largest-time-for-given-digits/)

```py title=largest-time-for-given-digits.py
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        for perm in permutations(sorted(arr, reverse = 1)):
            if perm[0] * 10 + perm[1] < 24 and perm[2] < 6:
                return f"{perm[0]}{perm[1]}:{perm[2]}{perm[3]}"
        
        return ""
```

```cpp title=largest-time-for-given-digits.cpp
class Solution {
public:
	string largestTimeFromDigits(vector<int>& A) {
		string ans = "";
		sort(A.begin(),A.end());
		do
		{
			if((A[0]==2 && A[1]<=3 || A[0]<2) && A[2]<=5)
			{
				string temp = to_string(A[0])+to_string(A[1])+":"
					+to_string(A[2])+to_string(A[3]);
				if(temp > ans) ans = temp;
			}       
		}while(next_permutation(A.begin(),A.end()));
		return ans;
	}
};

```


