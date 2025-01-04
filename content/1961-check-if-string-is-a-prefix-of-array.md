---
title: 1961. Check If String Is a Prefix of Array
draft: false
tags: 
  - leetcode-easy
  - array
  - two-pointers
  - string
date: 2021-08-08
---

[Problem Link](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/)

## Description

---
<p>Given a string <code>s</code> and an array of strings <code>words</code>, determine whether <code>s</code> is a <strong>prefix string</strong> of <code>words</code>.</p>

<p>A string <code>s</code> is a <strong>prefix string</strong> of <code>words</code> if <code>s</code> can be made by concatenating the first <code>k</code> strings in <code>words</code> for some <strong>positive</strong> <code>k</code> no larger than <code>words.length</code>.</p>

<p>Return <code>true</code><em> if </em><code>s</code><em> is a <strong>prefix string</strong> of </em><code>words</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;iloveleetcode&quot;, words = [&quot;i&quot;,&quot;love&quot;,&quot;leetcode&quot;,&quot;apples&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong>
s can be made by concatenating &quot;i&quot;, &quot;love&quot;, and &quot;leetcode&quot; together.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;iloveleetcode&quot;, words = [&quot;apples&quot;,&quot;i&quot;,&quot;love&quot;,&quot;leetcode&quot;]
<strong>Output:</strong> false
<strong>Explanation:</strong>
It is impossible to make s using a prefix of arr.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>words[i]</code> and <code>s</code> consist of only lowercase English letters.</li>
</ul>


## Solution

---
### Python
``` py title='check-if-string-is-a-prefix-of-array'
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        
        for word in words:
            res += word
            
            if res == s: return True
        
        return False
```
