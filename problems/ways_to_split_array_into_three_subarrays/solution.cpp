class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        int M = 1e9 + 7;
        int n = nums.size();
        
        for (int i = 1; i < n; i++)
            nums[i] += nums[i-1];
        
        long long res = 0;
        for (int i = 0; i < n - 1; i++){
            int left = nums[i];
            int remaining = nums[n-1] - left;
            int max_mid = remaining / 2;
            
            int mid_start = lower_bound(nums.begin()+i+1, nums.end()-1, left * 2) - nums.begin();
            int right_start = upper_bound(nums.begin()+i+1, nums.end()-1, left + max_mid) - nums.begin();
            
            res += max(0, right_start - mid_start);
            res %= M;
        }
        
        return res % M;
    }
};