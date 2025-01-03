---
title: 2628. JSON Deep Equal
draft: false
tags: 

date: 2023-05-21
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='json-deep-equal'
function areDeeplyEqual(o1: any, o2: any): boolean {
    // All equal values and same objects are eliminated
    if (o1 === o2) return true;
    
    // If any of o1 or o2 is not an object, they are different values
    if (typeof o1 != 'object' || typeof o2 != 'object') return false;

    // Both of them should be objects or arrays
    if (Array.isArray(o1) !== Array.isArray(o2)) return false;
    
    // Both should have same keys, in case of indexes this will return indexes
    if (Object.keys(o1).length != Object.keys(o2).length) return false;

    // Check if all values against keys of o1 and o2 are deeply equal.
    // If number of keys are same, then at a different key in objects would mean at least
    // 1 value against the key of o2 will be undefined
    for (const key in o1) {
        if (!areDeeplyEqual(o1[key], o2[key])) return false;
    }

    // All checks passed
    return true;
};

```

