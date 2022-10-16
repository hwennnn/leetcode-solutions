class Solution {
public:
    int countPrimes(int n) {
        vector<bool> arr(n, false);
        int count = 0;
        
        if (n <=2){
            return 0;
        } 
        
       for (int i = 2; i < n; i++){
           if (!arr[i]){
               count++;
               
               for (int j = 2; i*j<=n; j++)
                   arr[i*j] = true;
           }
       }
        
        return count;
    }
};