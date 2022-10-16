class Solution {
public:
    int numOfSubarrays(vector<int>& A) {
        int cur = 0, odd = 0, even = 1, mod = (int)1e9 + 7, res = 0;
        for (int a: A) {
            cur += a;
            if (cur%2){
                res = (res+even)%mod;
                odd++;
            }else{
                res = (res+odd)%mod;
                even++;
            }
        }
        return res;
    }
        
};