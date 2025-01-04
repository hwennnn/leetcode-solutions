---
title: 28. Find the Index of the First Occurrence in a String
draft: false
tags: 
  - leetcode-easy
  - two-pointers
  - string
  - string-matching
date: 2020-08-29
---

[Problem Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

## Description

---
<p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>


## Solution

---
### Python
``` py title='find-the-index-of-the-first-occurrence-in-a-string'
class Solution:
    def strStr(self, s: str, target: str) -> int:
        if len(target) == 0 or s == target: return 0

        N, M = len(s), len(target)

        for i in range(N):
            for j in range(M):
                if i + j >= N or s[i + j] != target[j]: break

                if j == M - 1: return i

        return -1
```
### Java
``` java title='find-the-index-of-the-first-occurrence-in-a-string'
class Solution {
   public int strStr(String haystack, String needle) {
      for (int i = 0; ; i++) {
        for (int j = 0; ; j++) {
          if (j == needle.length()) return i;
          if (i + j == haystack.length()) return -1;
          if (needle.charAt(j) != haystack.charAt(i + j)) break;
        }
      }
    }
}
```

