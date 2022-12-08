---
id: numbers-with-repeated-digits
title: Numbers With Repeated Digits
description: Problem Description and Solution for Numbers With Repeated Digits
sidebar_label: 1012. Numbers With Repeated Digits
sidebar_position: 1012
---

# [1012. Numbers With Repeated Digits](https://leetcode.com/problems/numbers-with-repeated-digits/)

```py title=numbers-with-repeated-digits.py
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        
        def findNonRepeated(n):
            digits = []

            while n > 0:
                digits.append(n % 10)
                n //= 10

            digits.reverse()

            N = len(digits)

            @cache
            def dp(pos, tight, mask):
                if pos == N:
                    return 1 if mask != 0 else 0

                limit = digits[pos] if tight else 9
                res = 0

                for i in range(0, limit + 1):
                    if mask & (1 << i) > 0: continue

                    nextTight = tight and i == digits[pos]
                    nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)

                    res += dp(pos + 1, nextTight, nextMask)

                return res
            
            return dp(0, True, 0)
        
        return n - findNonRepeated(n)
```

```cpp title=numbers-with-repeated-digits.cpp
class Solution {
public:
    //dp[pos][tight][start][rep][mask];
    int dp[10][2][2][2][1<<10];
    vector<int>num;
    int solve(int pos,int tight,int start,int rep,int mask)
    {
        if(pos == num.size())
        {
            return rep;
        }
        int &ans= dp[pos][tight][start][rep][mask];
        if(ans!=-1)return ans;

        int k = num[pos];
        if(tight)k=9;
        int res=0;
        for(int i=0;i<=k;i++)
        {
            int ns = start||i>0;//number started yet or not
            int nt = tight||i<k;//tight for next number
            if(ns){
                res+=solve(pos+1,nt,ns,rep||(mask&(1<<i)),mask|1<<i);
            }
            else{
                res+=solve(pos+1,nt,0,rep,mask);
            }

        }
        ans= res;
        return res;
    }
    int numDupDigitsAtMostN(int N) {
        while(N){
            num.push_back(N%10);
            N/=10;
        }
        reverse(num.begin(),num.end());
        memset(dp,-1,sizeof(dp));
        return solve(0,0,0,0,0);
    }
};
```


