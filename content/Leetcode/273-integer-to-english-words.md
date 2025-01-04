---
title: 273. Integer to English Words
draft: false
tags: 
  - leetcode-hard
  - math
  - string
  - recursion
date: 2024-08-07
---

[Problem Link](https://leetcode.com/problems/integer-to-english-words/)

## Description

---
<p>Convert a non-negative integer <code>num</code> to its English words representation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 123
<strong>Output:</strong> &quot;One Hundred Twenty Three&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 12345
<strong>Output:</strong> &quot;Twelve Thousand Three Hundred Forty Five&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 1234567
<strong>Output:</strong> &quot;One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solution

---
### C++
``` cpp title='integer-to-english-words'
class Solution {
public:
    string one(int num) {
    switch(num) {
      case 1: return "One";
      case 2: return "Two";
      case 3: return "Three";
      case 4: return "Four";
      case 5: return "Five";
      case 6: return "Six";
      case 7: return "Seven";
      case 8: return "Eight";
      case 9: return "Nine";
    }
    return "";
  }

  string twoLessThan20(int num) {
    switch(num) {
      case 10: return "Ten";
      case 11: return "Eleven";
      case 12: return "Twelve";
      case 13: return "Thirteen";
      case 14: return "Fourteen";
      case 15: return "Fifteen";
      case 16: return "Sixteen";
      case 17: return "Seventeen";
      case 18: return "Eighteen";
      case 19: return "Nineteen";
    }
    return "";
  }

  string ten(int num) {
    switch(num) {
      case 2: return "Twenty";
      case 3: return "Thirty";
      case 4: return "Forty";
      case 5: return "Fifty";
      case 6: return "Sixty";
      case 7: return "Seventy";
      case 8: return "Eighty";
      case 9: return "Ninety";
    }
    return "";
  }

  string two(int num) {
    if (num == 0)
      return "";
    else if (num < 10)
      return one(num);
    else if (num < 20)
      return twoLessThan20(num);
    else {
      int tenner = num / 10;
      int rest = num - tenner * 10;
      if (rest != 0)
        return ten(tenner) + " " + one(rest);
      else
        return ten(tenner);
    }
  }

  string three(int num) {
    int hundred = num / 100;
    int rest = num - hundred * 100;
    string res = "";
    if (hundred*rest != 0)
      res = one(hundred) + " Hundred " + two(rest);
    else if ((hundred == 0) && (rest != 0))
      res = two(rest);
    else if ((hundred != 0) && (rest == 0))
      res = one(hundred) + " Hundred";
    return res;
  }

    string numberToWords(int num) {
        if (num == 0)
      return "Zero";

    int billion = num / 1000000000;
    int million = (num - billion * 1000000000) / 1000000;
    int thousand = (num - billion * 1000000000 - million * 1000000) / 1000;
    int rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000;

    string result = "";
    if (billion != 0)
      result = three(billion) + " Billion";
    if (million != 0) {
      if (result.size()!=0)
        result += " ";
      result += three(million) + " Million";
    }
    if (thousand != 0) {
      if (result.size()!=0)
        result += " ";
      result += three(thousand) + " Thousand";
    }
    if (rest != 0) {
      if (result.size()!=0)
        result += " ";
      result += three(rest);
    }
    return result;
    }

};
```

