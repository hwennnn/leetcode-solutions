class Solution {
public:
    int rob1(vector<int>& nums){
        int n = nums.size();
        
        int rob = 0, not_rob = 0;
        for (int i = 0; i < n-1; i++){
            int yes = not_rob + nums[i];
            int no = max(rob, not_rob);
            
            rob = yes;
            not_rob = no;
        }
        
        return max(rob, not_rob);
    }
    
    int rob2(vector<int>& nums){
        int n = nums.size();
        
        int rob = 0, not_rob = 0;
        for (int i = 1; i < n; i++){
            int yes = not_rob + nums[i];
            int no = max(rob, not_rob);
            
            rob = yes;
            not_rob = no;
        }
        
        return max(rob, not_rob);
    }
    
    int rob(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        return max(rob1(nums), rob2(nums));
    }
};