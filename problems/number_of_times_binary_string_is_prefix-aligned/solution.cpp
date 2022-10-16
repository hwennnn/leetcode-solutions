class Solution {
public:
    int numTimesAllBlue(vector<int>& light) {
        int right = 0, res = 0;

        for (int i = 0; i < light.size(); i++){
            right = max(right, light[i]);
            res += (right == i + 1);
        }
        
        return res;
    }
};