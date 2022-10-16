class Solution {
public:
    int minSetSize(vector<int>& arr) {
    unordered_map<int, int> m;
    multiset<int, greater <int>> s;        
    for (auto n : arr) ++m[n];
    for (auto &p : m) s.insert(p.second);
    int res = 0, cnt = 0;
    for (auto it = begin(s); cnt * 2 < arr.size(); ++it) {
        ++res;
        cnt += *it;
    }
    return res;
}
};