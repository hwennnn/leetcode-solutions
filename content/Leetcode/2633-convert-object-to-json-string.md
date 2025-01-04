---
title: 2633. Convert Object to JSON String
draft: false
tags: 
  - leetcode-medium
date: 2023-05-22
---

[Problem Link](https://leetcode.com/problems/convert-object-to-json-string/)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='convert-object-to-json-string'
function jsonStringify(object: any): string {
    if (object === null) return "null";

    if (typeof object === 'string') {
        return `"${object}"`;
    }

    if (typeof object === 'number' || typeof object === 'boolean') {
        return object.toString();
    }

    if (Array.isArray(object)) {
        const items = object.map((item) => jsonStringify(item)).join(',');

        return `[${items}]`;
    }

    if (typeof object === 'object') {
        const keys = Object.keys(object);
        const items = keys.map((key) => `"${key}":${jsonStringify(object[key])}`).join(',');

        return `{${items}}`;
    }
};
```

