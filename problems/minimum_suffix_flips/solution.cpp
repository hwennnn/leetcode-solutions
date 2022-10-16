class Solution {
public:
    int minFlips(string target) {
        int n = target.size();
        int flips = 0;
        char status = '0';
        
        for (int i = 0; i < n; i++){
            
            if (target[i] != status){
                flips++;
                
                status = status == '0' ? '1' : '0';
            }
                
        }
        
        return flips;
            
           
    }
};