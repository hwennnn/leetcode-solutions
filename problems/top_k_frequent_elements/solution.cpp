class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for (int num: nums)
            ++mp[num];
        
        
        vector<vector<int>> buckets(nums.size() + 1); 
        for (auto v: mp)
            buckets[v.second].push_back(v.first);
        
        
        vector<int> res;
        for (int i = buckets.size() - 1; i >= 0 && res.size() < k; --i){
            for (int num : buckets[i]){
                res.push_back(num);
                
                if (res.size() == k)
                    break;
            }
        }
        
        return res;
    }
};