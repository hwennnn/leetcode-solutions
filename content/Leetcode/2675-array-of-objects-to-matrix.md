---
title: 2675. Array of Objects to Matrix
draft: false
tags: 
  - leetcode-hard
date: 2023-05-23
---

[Problem Link](https://leetcode.com/problems/array-of-objects-to-matrix/)

## Description

---
null

## Solution

---
### TypeScript
``` ts title='array-of-objects-to-matrix'
function jsonToMatrix(arr: any[]): (string | number | boolean | null)[][] {
  const flattenObject = (obj: any, prefix = ""): Record<string, any> => {
    let result: Record<string, any> = {};

    for (let key in obj) {
      let value = obj[key];

      if (typeof value === "object" && value !== null) {
        let flattened = flattenObject(value, prefix + key + ".");
        result = { ...result, ...flattened };
      } else {
        result[prefix + key] = value;
      }
    }

    return result;
  };

  let flattenedArr = arr.map(obj => flattenObject(obj));

  let columnSet = new Set<string>();
  flattenedArr.forEach(obj => {
    Object.keys(obj).forEach(key => columnSet.add(key));
  });

  let columns = Array.from(columnSet).sort();
  let matrix: (string | number | boolean | null)[][] = [columns];

  flattenedArr.forEach(obj => {
    let row = columns.map(key => (obj[key] !== undefined ? obj[key] : ""));
    matrix.push(row);
  });

  return matrix;
}
```

