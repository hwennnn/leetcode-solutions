class Solution {
public:
    //dp[pos][tight][start][rep][mask];
    int dp[10][2][2][2][1<<10];
    vector<int>num;
    int solve(int pos,int tight,int start,int rep,int mask)
    {
        if(pos == num.size())
        {
            return rep;
        }
        int &ans= dp[pos][tight][start][rep][mask];
        if(ans!=-1)return ans;

        int k = num[pos];
        if(tight)k=9;
        int res=0;
        for(int i=0;i<=k;i++)
        {
            int ns = start||i>0;//number started yet or not
            int nt = tight||i<k;//tight for next number
            if(ns){
                res+=solve(pos+1,nt,ns,rep||(mask&(1<<i)),mask|1<<i);
            }
            else{
                res+=solve(pos+1,nt,0,rep,mask);
            }

        }
        ans= res;
        return res;
    }
    int numDupDigitsAtMostN(int N) {
        while(N){
            num.push_back(N%10);
            N/=10;
        }
        reverse(num.begin(),num.end());
        memset(dp,-1,sizeof(dp));
        return solve(0,0,0,0,0);
    }
};