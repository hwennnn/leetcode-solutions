class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        
        string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        lst = []

        for i in words:
            i_str = ""
            for x in i:
                str_index = string.index(x)
                i_str+=table[str_index]  
            lst.append(i_str)

        another_lst = []
        
        for i in lst:
            if i not in another_lst:
                another_lst.append(i)
        
        return len(another_lst)
    
        
        
            