class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        res = []
        lst=  []
        
        for i in arr:
            if i not in res:
                res.append(i)
                
        for i in range(len(res)):
            lst.append(arr.count(res[i]))
        
        check_lst = []
        for i in range(len(lst)):
            if i>0:
                if lst[i-1] == lst[i]:
                    break
            check_lst.append(lst.count(lst[i]))
        
        for i in check_lst:
            if i>1:
                return False
            
        return True
        
        
       