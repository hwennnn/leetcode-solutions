class Solution {
public:
    int clumsy(int n) {
        stack<int> s;
        s.push(n--);
        
        while (n > 0) {
            int top = s.top();
            s.pop();
            s.push(top * n--);
            
            if (n > 0) {
                int top = s.top();
                s.pop();
                s.push(top / n--);
            }
            
            if (n > 0) {
                s.push(n--);
            }
            
            if (n > 0) {
                s.push(-1 * n--);
            }
        }
        
        int res = 0;
        
        while (s.size() > 0) {
            int top = s.top();
            s.pop();
            res += top;
        }
        
        return res;
    }
};