class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n-2; i++){
            
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            
            int l = i+1, r = n-1;
            
            while (l < r){
                int s = nums[i] + nums[l] + nums[r];
                
                if (s < 0)
                    l++;
                
                else if (s > 0)
                    r--;
                
                else{
                    vector<int> temp(3, 0);
                    temp[0] = nums[i];
                    temp[1] = nums[l];
                    temp[2] = nums[r];
                    res.push_back(temp);
                    
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    
                    l++;
                    r--;
                }
            }         
        }
        return res;
    }
};