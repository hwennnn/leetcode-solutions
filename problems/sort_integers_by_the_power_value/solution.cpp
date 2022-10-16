class Solution {
    #define ar array
public:
    int getKth(int lo, int hi, int k) {
        vector<ar<int,2>> mp;
        
        for (int i = lo; i <= hi; i++){
            mp.push_back({0,i});
            int j = i;
            while (j > 1){
                if (j&1)
                    j = 3 * j + 1;
                else
                    j = j / 2;
                ++mp.back()[0];
            }
        }
        
        sort(mp.begin(), mp.end());
        
        return mp[k-1][1];
    }
};