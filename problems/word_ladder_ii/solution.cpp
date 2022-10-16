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