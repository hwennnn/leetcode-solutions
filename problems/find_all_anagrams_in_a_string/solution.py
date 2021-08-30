class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = collections.Counter(p)
        required = len(p)
        start = 0
        res = []
        
        for end, c in enumerate(s):
            if c in counter:
                if counter[c] > 0:
                    required -= 1
                counter[c] -= 1

            while required == 0:
                if s[start] in counter:
                    counter[s[start]] += 1
                    if counter[s[start]] > 0:
                        required += 1
                if end - start + 1 == len(p):
                    res.append(start)
                start += 1
        
        return res
# public class Solution {
# public List<Integer> findAnagrams(String s, String t) {
#     List<Integer> result = new LinkedList<>();
#     if(t.length()> s.length()) return result;
#     Map<Character, Integer> map = new HashMap<>();
#     for(char c : t.toCharArray()){
#         map.put(c, map.getOrDefault(c, 0) + 1);
#     }
#     int counter = map.size();

#     int begin = 0, end = 0;
#     int head = 0;
#     int len = Integer.MAX_VALUE;


#     while(end < s.length()){
#         char c = s.charAt(end);
#         if( map.containsKey(c) ){
#             map.put(c, map.get(c)-1);
#             if(map.get(c) == 0) counter--;
#         }
#         end++;

#         while(counter == 0){
#             char tempc = s.charAt(begin);
#             if(map.containsKey(tempc)){
#                 map.put(tempc, map.get(tempc) + 1);
#                 if(map.get(tempc) > 0){
#                     counter++;
#                 }
#             }
#             if(end-begin == t.length()){
#                 result.add(begin);
#             }
#             begin++;
#         }

#     }
#     return result;
# }
# }