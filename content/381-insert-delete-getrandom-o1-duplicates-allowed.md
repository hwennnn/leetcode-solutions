---
title: 381. Insert Delete GetRandom O(1) - Duplicates allowed
draft: false
tags: 
  - leetcode-hard
  - array
  - hash-table
  - math
  - design
  - randomized
date: 2021-10-21
---

[Problem Link](https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)

## Description

---
<p><code>RandomizedCollection</code> is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.</p>

<p>Implement the <code>RandomizedCollection</code> class:</p>

<ul>
	<li><code>RandomizedCollection()</code> Initializes the empty <code>RandomizedCollection</code> object.</li>
	<li><code>bool insert(int val)</code> Inserts an item <code>val</code> into the multiset, even if the item is already present. Returns <code>true</code> if the item is not present, <code>false</code> otherwise.</li>
	<li><code>bool remove(int val)</code> Removes an item <code>val</code> from the multiset if present. Returns <code>true</code> if the item is present, <code>false</code> otherwise. Note that if <code>val</code> has multiple occurrences in the multiset, we only remove one of them.</li>
	<li><code>int getRandom()</code> Returns a random element from the current multiset of elements. The probability of each element being returned is <strong>linearly related</strong> to the number of the same values the multiset contains.</li>
</ul>

<p>You must implement the functions of the class such that each function works on <strong>average</strong> <code>O(1)</code> time complexity.</p>

<p><strong>Note:</strong> The test cases are generated such that <code>getRandom</code> will only be called if there is <strong>at least one</strong> item in the <code>RandomizedCollection</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;RandomizedCollection&quot;, &quot;insert&quot;, &quot;insert&quot;, &quot;insert&quot;, &quot;getRandom&quot;, &quot;remove&quot;, &quot;getRandom&quot;]
[[], [1], [1], [2], [], [1], []]
<strong>Output</strong>
[null, true, false, true, 2, true, 1]

<strong>Explanation</strong>
RandomizedCollection randomizedCollection = new RandomizedCollection();
randomizedCollection.insert(1);   // return true since the collection does not contain 1.
                                  // Inserts 1 into the collection.
randomizedCollection.insert(1);   // return false since the collection contains 1.
                                  // Inserts another 1 into the collection. Collection now contains [1,1].
randomizedCollection.insert(2);   // return true since the collection does not contain 2.
                                  // Inserts 2 into the collection. Collection now contains [1,1,2].
randomizedCollection.getRandom(); // getRandom should:
                                  // - return 1 with probability 2/3, or
                                  // - return 2 with probability 1/3.
randomizedCollection.remove(1);   // return true since the collection contains 1.
                                  // Removes 1 from the collection. Collection now contains [1,2].
randomizedCollection.getRandom(); // getRandom should return 1 or 2, both equally likely.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;= val &lt;= 2<sup>31</sup> - 1</code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls <strong>in total</strong> will be made to <code>insert</code>, <code>remove</code>, and <code>getRandom</code>.</li>
	<li>There will be <strong>at least one</strong> element in the data structure when <code>getRandom</code> is called.</li>
</ul>


## Solution

---
### Python3
``` py title='insert-delete-getrandom-o1-duplicates-allowed'
class RandomizedCollection:

    def __init__(self):
        self.mp = collections.defaultdict(list)
        self.A = []
        
    def insert(self, val: int) -> bool:
        isExist = len(self.mp[val]) == 0
        
        self.mp[val].append(len(self.A))
        self.A.append((val, len(self.mp[val]) - 1))
        
        return isExist

    def remove(self, val: int) -> bool:
        if len(self.mp[val]) == 0: return False
        
        last = self.A[-1]
        self.mp[last[0]][last[1]] = self.mp[val][-1]
        self.A[self.mp[val].pop()] = last
        self.A.pop()
        
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.A)[0]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

