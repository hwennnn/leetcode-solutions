class Solution {
    int a[15],f[32768],o[32768];
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
        memset(a,0,sizeof(a));
        int i,j,l;
        for(auto e:dependencies)a[e[1]-1]|=1<<e[0]-1;
        for(i=1;i<1<<n;i++)o[i]=o[i>>1]+(i&1);
        memset(f,127,sizeof(f));
        for(i=f[0]=0;i<1<<n;i++)if(f[i]<=n)
        {
            for(j=l=0;j<n;j++)if(!(i>>j&1)&&(a[j]&i)==a[j])l|=1<<j;
            for(j=l;j;j=j-1&l)if(o[j]<=k)f[i|j]=min(f[i|j],f[i]+1);
        }
        return f[(1<<n)-1];
    }
};