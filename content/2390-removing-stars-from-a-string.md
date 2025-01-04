---
title: 2390. Removing Stars From a String
draft: false
tags: 
  - leetcode-medium
  - string
  - stack
  - simulation
date: 2023-04-11
---

[Problem Link](https://leetcode.com/problems/removing-stars-from-a-string/)

## Description

---
<p>You are given a string <code>s</code>, which contains stars <code>*</code>.</p>

<p>In one operation, you can:</p>

<ul>
	<li>Choose a star in <code>s</code>.</li>
	<li>Remove the closest <strong>non-star</strong> character to its <strong>left</strong>, as well as remove the star itself.</li>
</ul>

<p>Return <em>the string after <strong>all</strong> stars have been removed</em>.</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The input will be generated such that the operation is always possible.</li>
	<li>It can be shown that the resulting string will always be unique.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leet**cod*e&quot;
<strong>Output:</strong> &quot;lecoe&quot;
<strong>Explanation:</strong> Performing the removals from left to right:
- The closest character to the 1<sup>st</sup> star is &#39;t&#39; in &quot;lee<strong><u>t</u></strong>**cod*e&quot;. s becomes &quot;lee*cod*e&quot;.
- The closest character to the 2<sup>nd</sup> star is &#39;e&#39; in &quot;le<strong><u>e</u></strong>*cod*e&quot;. s becomes &quot;lecod*e&quot;.
- The closest character to the 3<sup>rd</sup> star is &#39;d&#39; in &quot;leco<strong><u>d</u></strong>*e&quot;. s becomes &quot;lecoe&quot;.
There are no more stars, so we return &quot;lecoe&quot;.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;erase*****&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> The entire string is removed, so we return an empty string.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of lowercase English letters and stars <code>*</code>.</li>
	<li>The operation above can be performed on <code>s</code>.</li>
</ul>


## Solution

---
### Python
``` py title='removing-stars-from-a-string'
class Solution:
    def removeStars(self, s: str) -> str: 
        stack = []

        for x in s:
            if x == "*":
                stack.pop()
            else:
                stack.append(x)
        
        return "".join(stack)
```
