class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        vector<int> res;
        auto sub_sum = 0, half_sum = accumulate(begin(nums), end(nums), 0) / 2;
        priority_queue<int> pq(begin(nums), end(nums));
        while (sub_sum <= half_sum) {
            res.push_back(pq.top());
            sub_sum += res.back();
            pq.pop();
        }
        return res;
    }
};