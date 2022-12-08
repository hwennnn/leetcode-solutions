---
id: subdomain-visit-count
title: Subdomain Visit Count
description: Problem Description and Solution for Subdomain Visit Count
sidebar_label: 811. Subdomain Visit Count
sidebar_position: 811
---

# [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)

```py title=subdomain-visit-count.py
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = collections.defaultdict(int)
        
        for domain in cpdomains:
            count, url = domain.split()
            s = url.split('.')
            for i in range(len(s)):
                mp[".".join(s[i:])] += int(count)
        
        res = []
        
        for k, v in mp.items():
            res.append(f'{v} {k}')
        
        return res
```


