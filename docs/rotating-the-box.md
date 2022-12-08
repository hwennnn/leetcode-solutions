---
id: rotating-the-box
title: Rotating the Box
description: Problem Description and Solution for Rotating the Box
sidebar_label: 1861. Rotating the Box
sidebar_position: 1861
---

# [1861. Rotating the Box](https://leetcode.com/problems/rotating-the-box/)

```py title=rotating-the-box.py
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        
        for row in box:
            pos = cols - 1
            for j in range(cols - 1, -1, -1):
                if row[j] == '*':
                    pos = j - 1
                elif row[j] == '#':
                    row[j], row[pos] = row[pos], row[j]
                    pos -= 1
        
        return zip(*box[::-1])
```

```cpp title=rotating-the-box.cpp
// OJ: https://leetcode.com/contest/biweekly-contest-52/problems/rotating-the-box/
// Author: github.com/lzl124631x
// Time: O(MN)
// Space: O(1)
class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& A) {
        int M = A.size(), N = A[0].size();
        vector<vector<char>> ans(N, vector<char>(M, '.'));
        for (int i = 0; i < M; ++i) {
            int w = N - 1; // `w` is the write pointer
            for (int j = N - 1; j >= 0; --j) {
                if (A[i][j] == '.') continue;
                if (A[i][j] == '#') {
                    ans[w--][M - i - 1] = '#'; // write stone to position `(w, M - i - 1)` and move write pointer
                } else {
                    ans[j][M - i - 1] = '*';
                    w = j - 1; // move the writer pointer to the position after the obstacle
                }
            }
        }
        return ans;
    }
};
```


