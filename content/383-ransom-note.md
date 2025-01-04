---
title: 383. Ransom Note
draft: false
tags: 
  - leetcode-easy
  - hash-table
  - string
  - counting
date: 2022-08-25
---

[Problem Link](https://leetcode.com/problems/ransom-note/)

## Description

---
<p>Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code><em> if </em><code>ransomNote</code><em> can be constructed by using the letters from </em><code>magazine</code><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> ransomNote = "a", magazine = "b"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "ab"
<strong>Output:</strong> false
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> ransomNote = "aa", magazine = "aab"
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= ransomNote.length, magazine.length &lt;= 10<sup>5</sup></code></li>
	<li><code>ransomNote</code> and <code>magazine</code> consist of lowercase English letters.</li>
</ul>


## Solution

---
### Python3
``` py title='ransom-note'
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = collections.Counter(ransomNote)
        n = len(mp)
        
        for word in magazine:
            mp[word] -= 1
            if mp[word] == 0:
                n -= 1
            
            if n == 0: return True
        
        return False
```

