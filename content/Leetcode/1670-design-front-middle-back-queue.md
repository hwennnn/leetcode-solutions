---
title: 1670. Design Front Middle Back Queue
draft: false
tags: 
  - array
  - linked-list
  - design
  - queue
  - data-stream
date: 2024-07-20
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>Design a queue that supports <code>push</code> and <code>pop</code> operations in the front, middle, and back.</p>

<p>Implement the <code>FrontMiddleBack</code> class:</p>

<ul>
	<li><code>FrontMiddleBack()</code> Initializes the queue.</li>
	<li><code>void pushFront(int val)</code> Adds <code>val</code> to the <strong>front</strong> of the queue.</li>
	<li><code>void pushMiddle(int val)</code> Adds <code>val</code> to the <strong>middle</strong> of the queue.</li>
	<li><code>void pushBack(int val)</code> Adds <code>val</code> to the <strong>back</strong> of the queue.</li>
	<li><code>int popFront()</code> Removes the <strong>front</strong> element of the queue and returns it. If the queue is empty, return <code>-1</code>.</li>
	<li><code>int popMiddle()</code> Removes the <strong>middle</strong> element of the queue and returns it. If the queue is empty, return <code>-1</code>.</li>
	<li><code>int popBack()</code> Removes the <strong>back</strong> element of the queue and returns it. If the queue is empty, return <code>-1</code>.</li>
</ul>

<p><strong>Notice</strong> that when there are <b>two</b> middle position choices, the operation is performed on the <strong>frontmost</strong> middle position choice. For example:</p>

<ul>
	<li>Pushing <code>6</code> into the middle of <code>[1, 2, 3, 4, 5]</code> results in <code>[1, 2, <u>6</u>, 3, 4, 5]</code>.</li>
	<li>Popping the middle from <code>[1, 2, <u>3</u>, 4, 5, 6]</code> returns <code>3</code> and results in <code>[1, 2, 4, 5, 6]</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[&quot;FrontMiddleBackQueue&quot;, &quot;pushFront&quot;, &quot;pushBack&quot;, &quot;pushMiddle&quot;, &quot;pushMiddle&quot;, &quot;popFront&quot;, &quot;popMiddle&quot;, &quot;popMiddle&quot;, &quot;popBack&quot;, &quot;popFront&quot;]
[[], [1], [2], [3], [4], [], [], [], [], []]
<strong>Output:</strong>
[null, null, null, null, null, 1, 3, 4, 2, -1]

<strong>Explanation:</strong>
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [<u>1</u>]
q.pushBack(2);    // [1, <u>2</u>]
q.pushMiddle(3);  // [1, <u>3</u>, 2]
q.pushMiddle(4);  // [1, <u>4</u>, 3, 2]
q.popFront();     // return 1 -&gt; [4, 3, 2]
q.popMiddle();    // return 3 -&gt; [4, 2]
q.popMiddle();    // return 4 -&gt; [2]
q.popBack();      // return 2 -&gt; []
q.popFront();     // return -1 -&gt; [] (The queue is empty)
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= val &lt;= 10<sup>9</sup></code></li>
	<li>At most&nbsp;<code>1000</code>&nbsp;calls will be made to&nbsp;<code>pushFront</code>,&nbsp;<code>pushMiddle</code>,&nbsp;<code>pushBack</code>, <code>popFront</code>, <code>popMiddle</code>, and <code>popBack</code>.</li>
</ul>


## Solution

---
### C++
``` cpp title='design-front-middle-back-queue'
class FrontMiddleBackQueue {
    deque<int> a, b;

    void a2b() {
        if (a.size() <= b.size()) return;
        b.push_front(a.back());
        a.pop_back();
    }

    void b2a() {
        if (b.size() <= a.size() + 1) return;
        a.push_back(b.front());
        b.pop_front();
    }

public:
    FrontMiddleBackQueue() {
        
    }
    
    void pushFront(int val) {
        a.push_front(val);
        a2b();
    }
    
    void pushMiddle(int val) {
        a.push_back(val);
        a2b();
    }
    
    void pushBack(int val) {
        b.push_back(val);
        b2a();
    }
    
    int popFront() {
        if (a.empty() && b.empty()) return -1;

        int ans;

        if (a.empty()) {
            ans = b.front();
            b.pop_front();
        } else {
            ans = a.front();
            a.pop_front();
            b2a();
        }

        return ans;
    }
    
    int popMiddle() {
        if (a.empty() && b.empty()) return -1;

        int ans;

        if (a.size() == b.size()) {
            ans = a.back();
            a.pop_back();
        } else {
            ans = b.front();
            b.pop_front();
        }

        return ans;
    }
    
    int popBack() {
        if (a.empty() && b.empty()) return -1;

        int ans = b.back();
        b.pop_back();
        a2b();

        return ans;
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */

```

