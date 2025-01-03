---
title: 307. Range Sum Query - Mutable
draft: false
tags: 
  - array
  - design
  - binary-indexed-tree
  - segment-tree
date: 2023-10-31
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>Given an integer array <code>nums</code>, handle multiple queries of the following types:</p>

<ol>
	<li><strong>Update</strong> the value of an element in <code>nums</code>.</li>
	<li>Calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> where <code>left &lt;= right</code>.</li>
</ol>

<p>Implement the <code>NumArray</code> class:</p>

<ul>
	<li><code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.</li>
	<li><code>void update(int index, int val)</code> <strong>Updates</strong> the value of <code>nums[index]</code> to be <code>val</code>.</li>
	<li><code>int sumRange(int left, int right)</code> Returns the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> (i.e. <code>nums[left] + nums[left + 1] + ... + nums[right]</code>).</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;NumArray&quot;, &quot;sumRange&quot;, &quot;update&quot;, &quot;sumRange&quot;]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
<strong>Output</strong>
[null, 9, null, 8]

<strong>Explanation</strong>
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>0 &lt;= index &lt; nums.length</code></li>
	<li><code>-100 &lt;= val &lt;= 100</code></li>
	<li><code>0 &lt;= left &lt;= right &lt; nums.length</code></li>
	<li>At most <code>3 * 10<sup>4</sup></code> calls will be made to <code>update</code> and <code>sumRange</code>.</li>
</ul>


## Solution

---
### Python
``` py title='range-sum-query-mutable'
class LazySegmentTree:
  def __init__(self, arr):
    self.n = len(arr)
    self.tree = [0] * (4 * self.n)		
    self.lazy = [0] * (4 * self.n)
    self.build(1, 0, self.n - 1, arr)

  def build(self, v, tl, tr, arr):
    if tl == tr:
      self.tree[v] = arr[tl]
    else:
      tm = tl + (tr - tl) // 2
      self.build(v * 2, tl, tm, arr)
      self.build(v * 2 + 1, tm + 1, tr, arr)
      self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

  def query(self, v, tl, tr, l, r):
    self.lazy_update(v, tl, tr)
    
    if l > r: return 0

    if tl == l and tr == r:
      return self.tree[v]
    else:
      tm = tl + (tr - tl) // 2

      return self.query(v * 2, tl, tm, l, min(tm, r)) + self.query(v * 2 + 1, tm + 1, tr, max(tm + 1, l), r)

  def lazy_update(self, v, tl, tr):
    if self.lazy[v] != 0:
      self.tree[v] += (tr - tl + 1) * self.lazy[v]

      if tl != tr:
        self.lazy[v * 2] += self.lazy[v]
        self.lazy[v * 2 + 1] += self.lazy[v]

      self.lazy[v] = 0

  def range_update(self, v, tl, tr, l, r, value):
    self.lazy_update(v, tl, tr)
    
    if l > r: return
      
    if tl == l and tr == r:
      self.lazy[v] += value
      self.lazy_update(v, tl, tr)
    else:
      tm = tl + (tr - tl) // 2
      
      self.range_update(v * 2, tl, tm, l, min(tm, r), value)
      self.range_update(v * 2 + 1, tm + 1, tr, max(tm + 1, l), r, value)
      self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
    
  
  def update(self, v, tl, tr, pos, value):
    self.lazy_update(v, tl, tr)
    
    if tl == tr:
      self.tree[v] = value
    else:
      tm = tl + (tr - tl) // 2

      if pos <= tm:
        self.update(v * 2, tl, tm, pos, value)
      else:
        self.update(v * 2 + 1, tm + 1, tr, pos, value)

      self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

class NumArray:

    def __init__(self, nums: List[int]):
        self.st = LazySegmentTree(nums)
        self.n = len(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(1, 0, self.n - 1, index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

```

