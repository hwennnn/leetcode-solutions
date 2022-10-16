class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            bool illegal = false;
            for (int j = 0; j < n; ++j)
                if (i >> j&1){
                    if (j > 0 && nums[j]==nums[j-1] && (i>>(j-1)&1) == 0){
                        illegal = true;
                        break;
                    }else{
                        c.push_back(nums[j]);
                    }
                }
                    
            if (!illegal){
                res.push_back(c);
            }
        }
        
        return res;
    }
};