---
title: 844. Backspace String Compare
draft: false
tags: 
  - two-pointers
  - string
  - stack
  - simulation
date: 2023-10-19
---

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-blue.svg)

## Description

---
<p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if they are equal when both are typed into empty text editors</em>. <code>&#39;#&#39;</code> means a backspace character.</p>

<p>Note that after backspacing an empty text, the text will continue empty.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab#c&quot;, t = &quot;ad#c&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become &quot;ac&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab##&quot;, t = &quot;c#d#&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> Both s and t become &quot;&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a#c&quot;, t = &quot;b&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> s becomes &quot;c&quot; while t becomes &quot;b&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= s.length, t.length &lt;= 200</span></code></li>
	<li><span><code>s</code> and <code>t</code> only contain lowercase letters and <code>&#39;#&#39;</code> characters.</span></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it in <code>O(n)</code> time and <code>O(1)</code> space?</p>


## Solution

---
### Python
``` py title='backspace-string-compare'
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        M, N = len(s), len(t)
        i, j = M - 1, N - 1

        while True:
            delCount = 0
            while i >= 0 and (delCount > 0 or s[i] == "#"):
                if s[i] == '#':
                    delCount += 1
                else:
                    delCount -= 1
                i -= 1
            
            delCount = 0
            while j >= 0 and (delCount > 0 or t[j] == "#"):
                if t[j] == '#':
                    delCount += 1
                else:
                    delCount -= 1
                j -= 1
            
            if i >= 0 and j >= 0 and s[i] == t[j]:
                i -= 1
                j -= 1
            else:
                break
        
        return i == -1 and j == -1

  

```

