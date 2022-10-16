class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        int n = nums.size();
        int lastZero = -1;
        int firstNegative = -1;
        int res = 0;
        int neg = 0;
        
        for (int i = 0; i < n; i++){
            if (nums[i] < 0){
                 neg++;
                if (firstNegative == -1){
                    firstNegative = i;
                }
        
            }
            
            if (nums[i] == 0){
                neg = 0;
                firstNegative = -1;
                lastZero = i;
            }else{
                if (neg%2 == 0){
                    res = max(res, i - lastZero);
                }
                else{
                    res = max(res, i - firstNegative);
                }
            }
            
            
               
        }
        
        return res;
            
            
            
    }
};
