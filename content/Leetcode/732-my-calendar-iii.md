---
title: 732. My Calendar III
draft: false
tags: 
  - binary-search
  - design
  - segment-tree
  - prefix-sum
  - ordered-set
date: 2022-10-07
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>A <code>k</code>-booking happens when <code>k</code> events have some non-empty intersection (i.e., there is some time that is common to all <code>k</code> events.)</p>

<p>You are given some events <code>[startTime, endTime)</code>, after each given event, return an integer <code>k</code> representing the maximum <code>k</code>-booking between all the previous events.</p>

<p>Implement the <code>MyCalendarThree</code> class:</p>

<ul>
	<li><code>MyCalendarThree()</code> Initializes the object.</li>
	<li><code>int book(int startTime, int endTime)</code> Returns an integer <code>k</code> representing the largest integer such that there exists a <code>k</code>-booking in the calendar.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyCalendarThree&quot;, &quot;book&quot;, &quot;book&quot;, &quot;book&quot;, &quot;book&quot;, &quot;book&quot;, &quot;book&quot;]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
<strong>Output</strong>
[null, 1, 1, 2, 3, 3, 3]

<strong>Explanation</strong>
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15); // return 3
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3

</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= startTime &lt; endTime &lt;= 10<sup>9</sup></code></li>
	<li>At most <code>400</code> calls will be made to <code>book</code>.</li>
</ul>


## Solution

---
### Python
``` py title='my-calendar-iii'
class LazySegmentTree:
    def __init__(self, low, high, val):
        self.low = low
        self.high = high
        self.val = val
        self.lazy = 0
        self.left = None
        self.right = None
    
    def _extend(self):
        if self.low < self.high:
            if self.left is None:
                mid = (self.low + self.high) // 2
                self.left = LazySegmentTree(self.low, mid, self.val)
                if mid + 1 <= self.high:
                    self.right = LazySegmentTree(mid + 1, self.high, self.val)
            elif self.lazy != 0:
                self.left.val += self.lazy
                self.left.lazy += self.lazy
                self.right.val += self.lazy
                self.right.lazy += self.lazy
        self.lazy = 0
        
    def update(self, low, high, delta):
        if low > high or self.high < low or high < self.low:
            return
        if low <= self.low and self.high <= high:
            self.val += delta
            self.lazy += delta
            return
        self._extend()
        self.left.update(low, high, delta)
        self.right.update(low, high, delta)
        self.val = max(self.left.val, self.right.val)
    
    def query(self, low, high):
        if low > high or self.high < low or high < self.low:
            return 0
        if low <= self.low and self.high <= high:
            return self.val
        self._extend()
        return max(self.left.query(low, high), self.right.query(low, high))

class MyCalendarThree:

    def __init__(self):
        self.st = LazySegmentTree(0, 10 ** 9, 0)

    def book(self, start: int, end: int) -> int:
        self.st.update(start, end - 1, 1)
        
        return self.st.query(0, 10 ** 9)


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

```

