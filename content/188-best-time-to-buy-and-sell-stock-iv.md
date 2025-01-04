---
title: 188. Best Time to Buy and Sell Stock IV
draft: false
tags: 
  - leetcode-hard
  - array
  - dynamic-programming
date: 2022-09-10
---

[Problem Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)

## Description

---
<p>You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day, and an integer <code>k</code>.</p>

<p>Find the maximum profit you can achieve. You may complete at most <code>k</code> transactions: i.e. you may buy at most <code>k</code> times and sell at most <code>k</code> times.</p>

<p><strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 2, prices = [2,4,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 2, prices = [3,2,6,5,0,3]
<strong>Output:</strong> 7
<strong>Explanation:</strong> Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 100</code></li>
	<li><code>1 &lt;= prices.length &lt;= 1000</code></li>
	<li><code>0 &lt;= prices[i] &lt;= 1000</code></li>
</ul>


## Solution

---
### Python3
``` py title='best-time-to-buy-and-sell-stock-iv'
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        if k >= n // 2:
            res = 0
            
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            
            return res
        
        dp = [[0] * (n) for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            tempMax = -prices[0]
            
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + tempMax)
                tempMax = max(tempMax, dp[i - 1][j - 1] - prices[j])
        
        return dp[k][n - 1]
```

