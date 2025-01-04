---
title: 76. Minimum Window Substring
draft: false
tags: 
  - leetcode-hard
  - hash-table
  - string
  - sliding-window
date: 2024-08-13
---

[Problem Link](https://leetcode.com/problems/minimum-window-substring/)

## Description

---
<p>Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return <em>the <strong>minimum window</strong></em> <span data-keyword="substring-nonempty"><strong><em>substring</em></strong></span><em> of </em><code>s</code><em> such that every character in </em><code>t</code><em> (<strong>including duplicates</strong>) is included in the window</em>. If there is no such substring, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>The testcases will be generated such that the answer is <strong>unique</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>Output:</strong> &quot;BANC&quot;
<strong>Explanation:</strong> The minimum window substring &quot;BANC&quot; includes &#39;A&#39;, &#39;B&#39;, and &#39;C&#39; from string t.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
<strong>Explanation:</strong> The entire string s is the minimum window.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;, t = &quot;aa&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> Both &#39;a&#39;s from t must be included in the window.
Since the largest window of s only has one &#39;a&#39;, return empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>n == t.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> time?</p>


## Solution

---
### Python
``` py title='minimum-window-substring'
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        counter = Counter(t)
        length = len(counter)
        res = [inf, -1, -1]
        i = 0

        for j, x in enumerate(s):
            if x in counter:
                counter[x] -= 1
                if counter[x] == 0:
                    length -= 1
            
            while length == 0:
                windowLength = j - i + 1
                if windowLength < res[0]:
                    res = [windowLength, i, j]
                
                if s[i] in counter:
                    counter[s[i]] += 1
                    if counter[s[i]] > 0:
                        length += 1
                    
                i += 1
        
        if res[0] == inf: return ""

        return s[res[1] : res[2] + 1]
```
