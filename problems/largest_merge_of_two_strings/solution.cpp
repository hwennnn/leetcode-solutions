class Solution {
public:
    string largestMerge(string s, string t) {
        string ans;
        int i = 0, j = 0;
        while(i < s.size() && j < t.size()) {
            if(s.substr(i) >= t.substr(j)) {
                ans += s[i];
                ++i;
            } else {
                ans += t[j];
                ++j;
            }
        }
        while(i < s.size()) {
            ans += s[i];
            ++i;
        }
        while(j < t.size()) {
            ans += t[j];
            ++j;
        }
        return ans;
    }
};
