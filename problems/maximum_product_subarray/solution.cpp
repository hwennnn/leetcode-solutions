class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int localMax = nums[0]; 
        int localMin = nums[0]; 
        int maxProd = nums[0]; 
        for(int i = 1; i < nums.size(); i ++){ 
            if(nums[i] > 0){ 
                localMax = max(localMax * nums[i], nums[i]); 
                localMin = min(localMin * nums[i], nums[i]); 
            } else{ 
                int localMaxNeg = max(localMin * nums[i], nums[i]); 
                localMin = min(localMax * nums[i], nums[i]); 
                localMax = localMaxNeg; 
            } 
            maxProd = max(maxProd, localMax); 
        } 
        return maxProd; 
    }
};