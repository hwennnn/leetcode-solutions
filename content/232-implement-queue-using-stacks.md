---
title: 232. Implement Queue using Stacks
draft: false
tags: 
  - leetcode-easy
  - stack
  - design
  - queue
date: 2024-01-29
---

[Problem Link](https://leetcode.com/problems/implement-queue-using-stacks/)

## Description

---
<p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code>int pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code>int peek()</code> Returns the element at the front of the queue.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack&#39;s standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyQueue&quot;, &quot;push&quot;, &quot;push&quot;, &quot;peek&quot;, &quot;pop&quot;, &quot;empty&quot;]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code>&nbsp;calls will be made to <code>push</code>, <code>pop</code>, <code>peek</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>peek</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong><a href="https://en.wikipedia.org/wiki/Amortized_analysis" target="_blank">amortized</a></strong> <code>O(1)</code> time complexity? In other words, performing <code>n</code> operations will take overall <code>O(n)</code> time even if one of those operations may take longer.</p>


## Solution

---
### C++
``` cpp title='implement-queue-using-stacks'
class MyQueue {
public:
    stack<int> stack1, stack2;

    MyQueue() {
    }
    
    void push(int x) {
        stack1.push(x);
    }
    
    int pop() {
        peek();

        int e = stack2.top(); stack2.pop();
        return e;
    }
    
    int peek() {
        if (stack2.size() == 0) {
            while (stack1.size() > 0) {
                int e = stack1.top(); stack1.pop();
                stack2.push(e);
            }
        }

        return stack2.top();
    }
    
    bool empty() {
        return stack1.empty() && stack2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```
### Python
``` py title='implement-queue-using-stacks'
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]


    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
