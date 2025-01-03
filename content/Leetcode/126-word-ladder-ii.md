---
title: 126. Word Ladder II
draft: false
tags: 
  - hash-table
  - string
  - backtracking
  - breadth-first-search
date: 2022-08-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>A <strong>transformation sequence</strong> from word <code>beginWord</code> to word <code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words <code>beginWord -&gt; s<sub>1</sub> -&gt; s<sub>2</sub> -&gt; ... -&gt; s<sub>k</sub></code> such that:</p>

<ul>
	<li>Every adjacent pair of words differs by a single letter.</li>
	<li>Every <code>s<sub>i</sub></code> for <code>1 &lt;= i &lt;= k</code> is in <code>wordList</code>. Note that <code>beginWord</code> does not need to be in <code>wordList</code>.</li>
	<li><code>s<sub>k</sub> == endWord</code></li>
</ul>

<p>Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary <code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong> from</em> <code>beginWord</code> <em>to</em> <code>endWord</code><em>, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words </em><code>[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]
<strong>Output:</strong> [[&quot;hit&quot;,&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;cog&quot;],[&quot;hit&quot;,&quot;hot&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]]
<strong>Explanation:</strong>&nbsp;There are 2 shortest transformation sequences:
&quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;
&quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;lot&quot; -&gt; &quot;log&quot; -&gt; &quot;cog&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> beginWord = &quot;hit&quot;, endWord = &quot;cog&quot;, wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]
<strong>Output:</strong> []
<strong>Explanation:</strong> The endWord &quot;cog&quot; is not in wordList, therefore there is no valid transformation sequence.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= beginWord.length &lt;= 5</code></li>
	<li><code>endWord.length == beginWord.length</code></li>
	<li><code>1 &lt;= wordList.length &lt;= 500</code></li>
	<li><code>wordList[i].length == beginWord.length</code></li>
	<li><code>beginWord</code>, <code>endWord</code>, and <code>wordList[i]</code> consist of lowercase English letters.</li>
	<li><code>beginWord != endWord</code></li>
	<li>All the words in <code>wordList</code> are <strong>unique</strong>.</li>
	<li>The <strong>sum</strong> of all shortest transformation sequences does not exceed <code>10<sup>5</sup></code>.</li>
</ul>


## Solution

---
### C++
``` cpp title='word-ladder-ii'
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

