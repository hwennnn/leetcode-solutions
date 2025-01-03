---
title: 2700. Differences Between Two Objects
draft: false
tags: 

date: 2023-05-24
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='differences-between-two-objects'
function objDiff(obj1: any, obj2: any): any {
    function isObject(val) {
        return typeof val === 'object' && val !== null && !Array.isArray(val);
    }

    function compare(obj1, obj2, path, result) {
        if (isObject(obj1) && isObject(obj2)) {
        for (const key in obj1) {
            if (key in obj2) {
            compare(obj1[key], obj2[key], [...path, key], result);
            }
        }
        } else if (Array.isArray(obj1) && Array.isArray(obj2)) {
        const maxLength = Math.max(obj1.length, obj2.length);
        for (let i = 0; i < maxLength; i++) {
            if (i in obj1 && i in obj2) {
            compare(obj1[i], obj2[i], [...path, i], result);
            }
        }
        } else if (obj1 !== obj2) {
        if (path.length === 0) {
            result = [obj1, obj2];
        } else {
            let currentObj = result;
            for (let i = 0; i < path.length - 1; i++) {
            const key = path[i];
            if (!(key in currentObj)) {
                currentObj[key] = {};
            }
            currentObj = currentObj[key];
            }
            const lastKey = path[path.length - 1];
            currentObj[lastKey] = [obj1, obj2];
        }
        }
    }

    const result = {};
    compare(obj1, obj2, [], result);
    return result;
};

```

