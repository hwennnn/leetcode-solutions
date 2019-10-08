class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        lst = []
        for x in emails:
 
            res = ""
            a_index = x.index("@")
            try:
                var = x.index("+")
            except:
                var = None

            for i in range(len(x)):
                if var != None:
                    if var<=i<a_index:
                        continue
                if i < a_index:
                    if x[i] == "." :
                        continue
                    else:
                        res+=x[i]

                else:
                    res+=x[i]

            lst.append(res)
            

        return (len(set(lst)))
                    
                