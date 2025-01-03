---
title: 187. Repeated DNA Sequences
draft: false
tags: 
  - hash-table
  - string
  - bit-manipulation
  - sliding-window
  - rolling-hash
  - hash-function
date: 2021-11-03
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>The <strong>DNA sequence</strong> is composed of a series of nucleotides abbreviated as <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, and <code>&#39;T&#39;</code>.</p>

<ul>
	<li>For example, <code>&quot;ACGAATTCCG&quot;</code> is a <strong>DNA sequence</strong>.</li>
</ul>

<p>When studying <strong>DNA</strong>, it is useful to identify repeated sequences within the DNA.</p>

<p>Given a string <code>s</code> that represents a <strong>DNA sequence</strong>, return all the <strong><code>10</code>-letter-long</strong> sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
<strong>Output:</strong> ["AAAAACCCCC","CCCCCAAAAA"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "AAAAAAAAAAAAA"
<strong>Output:</strong> ["AAAAAAAAAA"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is either <code>&#39;A&#39;</code>, <code>&#39;C&#39;</code>, <code>&#39;G&#39;</code>, or <code>&#39;T&#39;</code>.</li>
</ul>


## Solution

---
### Python
``` py title='repeated-dna-sequences'
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = {"A": 1, "C": 2, "G": 3, "T": 4}
        q = (1 << 31) - 1
        h = (pow(4, 9)) % q
        seen, res = set(), set()
        t = 0
        
        for i, x  in enumerate(s):
            if i >= 10:
                t -= (mp[s[i - 10]] * h)
            t = (4 * t + mp[x]) % q

            if i >= 9 and t in seen:
                res.add(s[i - 9: i + 1])
            else:
                seen.add(t)
        
        return list(res)
        
        

```

