class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> deq;
        vector<int> res;
        
        for (int i = 0; i < nums.size(); i++){
            if (i >= k && deq.front() == nums[i-k])
                deq.pop_front();
            
            while (deq.size() > 0 && deq.back() < nums[i])
                deq.pop_back();
            
            deq.push_back(nums[i]);
            
            if (i >= k-1)
                res.push_back(deq.front());
            
        }
        
        return res;
    }
};