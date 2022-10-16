class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res, pos(26, 0);  
        for (auto i = 0; i < S.size(); ++i){
          pos[S[i] - 'a'] = i;
        }
        
        int maxIdx = INT_MIN, lastIdx = 0;
        
        for (auto i = 0; i < S.size(); i++){
            maxIdx = max(maxIdx, pos[S[i] - 'a']);
            if (i == maxIdx){
                res.push_back(maxIdx - lastIdx + 1);
                lastIdx = i + 1;
            }
        }
        
        return res;      
    }
};