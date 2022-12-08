---
id: word-ladder-ii
title: Word Ladder II
description: Problem Description and Solution for Word Ladder II
sidebar_label: 126. Word Ladder II
sidebar_position: 126
---

# [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)

```py title=word-ladder-ii.py
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res = []
        s = set(wordList)
        mmin = float('inf')
        queue = collections.deque([[beginWord]])
        level = 1
        visited = set()

        while queue:
            ladder = queue.popleft()
            n = len(ladder)
            
            if n > level:
                for v in visited:
                    s.remove(v)
                visited.clear()
                
                if n <= mmin:
                    level = n
                else:
                    break
                    
            word = ladder[-1]
            for i in range(len(word)):
                for w in string.ascii_lowercase:
                    newWord = word[:i] + w + word[i + 1:]
                    if newWord in s:
                        visited.add(newWord)
                        if newWord == endWord:
                            minLevel = n + 1
                            res.append(ladder + [newWord])
                        else:
                            queue.append((ladder + [newWord]))
                
        return res
```

```cpp title=word-ladder-ii.cpp
class Solution {
public:
    vector<vector<string>> findLadders(string s, string t, vector<string>& A) {
        
        set<string> st;
        for(auto a: A)
            st.insert(a);
        if(!st.count(t))
            return {};
            
        queue<pair<string, int>> q;
        q.push({s, 0});
        
        map<string, int> dp;
        dp[s] = 0;
        
        map<string, vector<string>> prv;
        
        while(!q.empty()) {
            auto [u, dpu] = q.front(); q.pop();
            
            if(dpu > dp[u])
                continue;
            
            int m = u.size();
            for(int i=0; i<m; i++) {
                char c = u[i];
                for(char d='a'; d<='z'; d++) {
                    if(c == d)
                        continue;
                    string v = u;
                    v[i] = d;
                    
                    if(!st.count(v))
                        continue;
                    if(!dp.count(v) || dpu + 1 < dp[v]) {
                        int dpv = dpu + 1;
                        q.push({v, dpv});
                        dp[v] = dpv;
                        
                        prv[v] = {u};
                    } else if(dpu + 1 == dp[v])
                        prv[v].push_back(u);
                }
            }
        }
        
        vector<vector<string>> ans;
        function<void (string, vector<string>&)> dfs=[&](string u, vector<string>&cur) {
            if(u == s) {
                reverse(cur.begin(), cur.end());
                ans.push_back(cur);
                reverse(cur.begin(), cur.end());
                return;
            }
            
            for(auto v: prv[u]) {
                cur.push_back(v);
                dfs(v, cur);
                cur.pop_back();
            }
        };
        vector<string> cur = {t};
        dfs(t, cur);
        
        return ans;
    }
};
```


