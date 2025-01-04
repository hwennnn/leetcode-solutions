---
title: 352. Data Stream as Disjoint Intervals
draft: false
tags: 
  - leetcode-hard
  - binary-search
  - design
  - ordered-set
date: 2023-01-28
---

[Problem Link](https://leetcode.com/problems/data-stream-as-disjoint-intervals/)

## Description

---
<p>Given a data stream input of non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code>, summarize the numbers seen so far as a list of disjoint intervals.</p>

<p>Implement the <code>SummaryRanges</code> class:</p>

<ul>
	<li><code>SummaryRanges()</code> Initializes the object with an empty stream.</li>
	<li><code>void addNum(int value)</code> Adds the integer <code>value</code> to the stream.</li>
	<li><code>int[][] getIntervals()</code> Returns a summary of the integers in the stream currently as a list of disjoint intervals <code>[start<sub>i</sub>, end<sub>i</sub>]</code>. The answer should be sorted by <code>start<sub>i</sub></code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;SummaryRanges&quot;, &quot;addNum&quot;, &quot;getIntervals&quot;, &quot;addNum&quot;, &quot;getIntervals&quot;, &quot;addNum&quot;, &quot;getIntervals&quot;, &quot;addNum&quot;, &quot;getIntervals&quot;, &quot;addNum&quot;, &quot;getIntervals&quot;]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
<strong>Output</strong>
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

<strong>Explanation</strong>
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= value &lt;= 10<sup>4</sup></code></li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>addNum</code> and <code>getIntervals</code>.</li>
	<li>At most <code>10<sup>2</sup></code>&nbsp;calls will be made to&nbsp;<code>getIntervals</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?</p>


## Solution

---
### Python3
``` py title='data-stream-as-disjoint-intervals'
class DSU:
    def __init__(self):
        self.p = {}
        self.intervals = {}

    def exists(self, x): return x in self.p

    def make_set(self, x):
        self.p[x] = x
        self.intervals[x] = [x,x]
        
    def find(self, x):
        if not self.exists(x): return None
        
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        
        if xr is None or yr is None: return
        
        self.p[xr] = yr
        
        ## interval adjusting logic
        x_interval = self.intervals[xr]
        del self.intervals[xr]
        
        self.intervals[yr] = [min(self.intervals[yr][0], x_interval[0]), max(self.intervals[yr][1], x_interval[1])]
        
class SummaryRanges:    
    def __init__(self):
        self.dsu = DSU()

    def addNum(self, val: int) -> None:
        if self.dsu.exists(val): return
            
        self.dsu.make_set(val)
        
        self.dsu.union(val, val-1)
        self.dsu.union(val, val+1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.dsu.intervals.values())

```

