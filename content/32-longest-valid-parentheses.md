---
title: 32. Longest Valid Parentheses
draft: false
tags: 
  - leetcode-hard
  - string
  - dynamic-programming
  - stack
date: 2022-05-24
---

[Problem Link](https://leetcode.com/problems/longest-valid-parentheses/)

## Description

---
<p>Given a string containing just the characters <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code>, return <em>the length of the longest valid (well-formed) parentheses </em><span data-keyword="substring-nonempty"><em>substring</em></span>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;(()&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;)()())&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest valid parentheses substring is &quot;()()&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;&quot;
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>s[i]</code> is <code>&#39;(&#39;</code>, or <code>&#39;)&#39;</code>.</li>
</ul>


## Solution

---
### Python3
``` py title='longest-valid-parentheses'
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        opened = []
        mp = [False] * n
        
        for i, c in enumerate(s):
            if c == "(":
                opened.append(i)
            else:
                if opened:
                    mp[opened.pop()] = True
                    mp[i] = True
        
        res = total = i = 0
        while i < n:
            if i + 1 < n and mp[i] and mp[i+1]:
                total += 2
                i += 2
            else:
                total = 0
                i += 1
            
            res = max(res, total)
    
        return res
                    
```

