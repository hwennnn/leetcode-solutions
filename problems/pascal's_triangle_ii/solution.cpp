class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int n = rowIndex+1;
        vector<int> tri(n,0);
        tri[0] = 1;
        
        
        for (int i = 1; i < n; i++){
             for (int j = i; j > 0; j--){
                 tri[j] += tri[j-1];
             }
        }
           
                
        
        return tri;
        
    }
};