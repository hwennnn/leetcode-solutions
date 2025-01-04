---
title: 345. Reverse Vowels of a String
draft: false
tags: 
  - leetcode-easy
  - two-pointers
  - string
date: 2022-11-04
---

[Problem Link](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Description

---
<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both lower and upper cases, more than once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;IceCreAm&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;AceCreIm&quot;</span></p>

<p><strong>Explanation:</strong></p>

<p>The vowels in <code>s</code> are <code>[&#39;I&#39;, &#39;e&#39;, &#39;e&#39;, &#39;A&#39;]</code>. On reversing the vowels, s becomes <code>&quot;AceCreIm&quot;</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;leetcode&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">&quot;leotcede&quot;</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul>


## Solution

---
### Python3
``` py title='reverse-vowels-of-a-string'
class Solution:
    def reverseVowels(self, s: str) -> str:
        N = len(s)
        s = list(s)
        i, j = 0, N - 1

        while i < j:
            while i < j and s[i] not in "aeiouAEIOU":
                i += 1
            
            while i < j and s[j] not in "aeiouAEIOU":
                j -= 1
            
            s[i], s[j] = s[j], s[i]
            
            i += 1
            j -= 1
        
        return "".join(s)
```

