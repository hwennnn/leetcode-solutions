class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            for (int j = 0; j < n; ++j)
                if (i >> j&1)
                    c.push_back(nums[j]);
            res.push_back(c);
        }
        
        return res;
    }
};