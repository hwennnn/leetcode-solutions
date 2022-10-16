class Solution {
public:
    string sortString(string s, string res = "") {
        int cnt[26] = {};
        for (auto ch : s)
            ++cnt[ch - 'a'];
        
        while (res.length() != s.length()){
            for (int i = 0; i < 26; i++)
                res += string(--cnt[i] >= 0 ? 1 : 0, 'a' + i);
            
            for (int i = 25; i >= 0; i--)
                res += string(--cnt[i] >= 0 ? 1 : 0, 'a' + i);
        }
        
        return res;
            
    }
};