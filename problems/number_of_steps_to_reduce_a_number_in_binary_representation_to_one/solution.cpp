class Solution { // my own simulation 
public:
    int numSteps(string s) {        
        int ans = 0;
        while(s!="1"){
            const int n = s.size();
            if(s[n-1]=='0'){       // using right shift to simulate divide in binary          
               // s=s.substr(0,n-1); //ok
                s.pop_back(); // better
            }else{                 // binary addition
                int i = n - 1;
                for(; i>=0 && s[i]!='0'; i--) s[i]='0';
                if(i>= 0) s[i]='1';
                else 
                    s = '1'+s;
                    //s.insert(s.begin(), '1'); //ok
                    //s.insert(0, 1,'1'); //ok
            }
            ans++;
        }
        return ans;
    }
}; 