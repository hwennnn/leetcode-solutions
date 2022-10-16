class Solution {
public:
    const int MAXN = 1e5 + 1, MOD = 1e9 + 7;
    int sumOfFlooredPairs(vector<int>& nums) {
        vector<long> freq(2*MAXN+1);        
        long mx = 0, sum = 0;
        for(auto num : nums) ++freq[num], mx = max((int)mx, num);  // counting frequency of each element in nums
        for(int i = 1; i <= 2*MAXN; ++i) freq[i] += freq[i - 1];   // building prefix sum array of freq. Now freq[i] will hold the frequency of numbers less than or equal to i
        // Each num will be assumed in the denominator as floor(nums[i] / num) and 
        // using freq array, we can calculate the number of terms contributing 1, 2, 3... to the sum each.
        for(auto num : nums) { 
            long l = num, r = 2 * num - 1, divResult = 1;
            while(l <= mx) {                
                sum = (sum + divResult * (freq[r] - freq[l - 1])) % MOD;
                l += num, r += num;
                ++divResult;
            }
        }
        return sum;
    }
};