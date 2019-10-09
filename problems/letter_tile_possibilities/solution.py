class Solution(object):
    def numTilePossibilities(self, tiles):
        s = "".join(set(tiles))
        ans = [] 

        for char in s:
            ans.append(char)    

        for elem in ans:
            temp = elem

            for char in s:
                temp += char
                if temp.count(char)<=tiles.count(char): 
                    ans.append(temp)
                temp = elem
                
        return len(set(ans))


        