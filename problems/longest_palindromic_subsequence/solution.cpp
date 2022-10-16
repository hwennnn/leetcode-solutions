class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> mem(n,vector<int>(n));
        
        return helper(0, n-1, s, mem);
    }
    
    int helper(int start, int end, string &s, vector<vector<int>> &mem){
        if (start == end) return 1;
        if (start > end) return 0 ;
        if (mem[start][end]) return mem[start][end];
        
        return mem[start][end] = s[start] == s[end] ? 2 + helper(start+1, end-1, s, mem) : 
        max(helper(start+1,end,s, mem), helper(start, end -1,s, mem));
    }
};