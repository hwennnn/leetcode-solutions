class Solution {
public:
    bool canPartition(vector<int>& nums) {
        bitset<10001> bits(1);
        int total = 0;
        
        for (auto n:nums)
            bits |= bits << n, total += n;
        
        return !(total&1) && bits[total / 2];
    }
};