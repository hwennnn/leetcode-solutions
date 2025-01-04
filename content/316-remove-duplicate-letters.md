---
title: 316. Remove Duplicate Letters
draft: false
tags: 
  - leetcode-medium
  - string
  - stack
  - greedy
  - monotonic-stack
date: 2023-09-26
---

[Problem Link](https://leetcode.com/problems/remove-duplicate-letters/)

## Description

---
<p>Given a string <code>s</code>, remove duplicate letters so that every letter appears once and only once. You must make sure your result is <span data-keyword="lexicographically-smaller-string"><strong>the smallest in lexicographical order</strong></span> among all possible results.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bcabc&quot;
<strong>Output:</strong> &quot;abc&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbacdcbc&quot;
<strong>Output:</strong> &quot;acdb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Note:</strong> This question is the same as 1081: <a href="https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/" target="_blank">https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/</a></p>


## Solution

---
### Python3
``` py title='remove-duplicate-letters'
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        stack = []
        put = set()

        for i, x in enumerate(s):
            count[x] -= 1
            if x in put: continue

            while stack and x < stack[-1] and count[stack[-1]] > 0:
                put.remove(stack.pop())
            
            stack.append(x)
            put.add(x)

        return "".join(stack)
```

