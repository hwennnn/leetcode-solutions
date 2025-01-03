---
title: 2632. Curry
draft: false
tags: 

date: 2023-05-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='curry'
function curry(fn: Function): Function {
    return function curried(...args) {
        if (args.length >= fn.length) {
            return fn(...args)
        } else {
            return (...args2) => curried(...args, ...args2);
        }
    };
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */

```

