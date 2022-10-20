# [943. Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring)

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg) ![Topics](https://img.shields.io/badge/Topics-Array,%20String,%20Dynamic%20Programming,%20Bit%20Manipulation,%20Bitmask-orange.svg)
<br/>

<p>Given an array of strings <code>words</code>, return <em>the smallest string that contains each string in</em> <code>words</code> <em>as a substring</em>. If there are multiple valid strings of the smallest length, return <strong>any of them</strong>.</p>

<p>You may assume that no string in <code>words</code> is a substring of another string in <code>words</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot;]
<strong>Output:</strong> &quot;alexlovesleetcode&quot;
<strong>Explanation:</strong> All permutations of &quot;alex&quot;,&quot;loves&quot;,&quot;leetcode&quot; would also be accepted.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;catg&quot;,&quot;ctaagt&quot;,&quot;gcta&quot;,&quot;ttca&quot;,&quot;atgcatc&quot;]
<strong>Output:</strong> &quot;gctaagttcatgcatc&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 12</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>words[i]</code> consists of lowercase English letters.</li>
	<li>All the strings of <code>words</code> are <strong>unique</strong>.</li>
</ul>

