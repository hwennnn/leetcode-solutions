class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        vector<int> dp {0,0,0}, dp2;
        
        for (int num : nums){
            dp2 = dp;
            
            for (int i : dp2){
                dp[(num+i)%3] = max(dp[(num+i)%3], num+i);
            }
        }
        
        return dp[0];
    }
};