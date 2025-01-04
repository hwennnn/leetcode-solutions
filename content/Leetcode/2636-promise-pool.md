---
title: 2636. Promise Pool
draft: false
tags: 
  - leetcode-medium
date: 2023-05-17
---

[Problem Link](https://leetcode.com/problems/promise-pool/)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='promise-pool'
type F = () => Promise<any>;

async function promisePool(functions: F[], n: number): Promise<any> {
    async function goNext() {
        if (functions.length == 0) return;

        const fn = functions.shift();
        await fn();
        await goNext();
    }

    await Promise.all(Array(n).fill(null).map(goNext))
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
```

