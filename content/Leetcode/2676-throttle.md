---
title: 2676. Throttle
draft: false
tags: 
  - leetcode-medium
date: 2023-05-20
---

[Problem Link](https://leetcode.com/problems/throttle/)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='throttle'
type F = (...args: any[]) => void

const throttle = (fn: F, t: number): F => {
    let pending = false;
    let nextArgs;
    const wrapper = (...args) => {
        nextArgs = args;
        if (!pending) {
            fn(...args);
            pending = true;
            nextArgs = undefined;
            setTimeout(() => {
                pending = false;
                if (nextArgs) wrapper(...nextArgs);
            }, t);
        }
    }
    return wrapper;
}

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
```

