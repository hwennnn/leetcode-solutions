class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> buckets(10001,0);
        
        for (int i = 0; i < nums.size(); i++){
            buckets[nums[i]] += nums[i];
        }
        
        vector<int> dp(10001,0);
        dp[0] = buckets[0];
        dp[1] = buckets[1];
        
        for (int i = 2; i < buckets.size(); i++){
            dp[i] = max(dp[i-1], buckets[i]+dp[i-2]);
        }
        
        return dp[10000];
    }
};