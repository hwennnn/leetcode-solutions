class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        isSelfDividing = True
        for i in range(left, right+1):
        # single digit
            if i < 10:
                ans.append(i)      
            # check if not contains 0, aka mod 10 != 0
            elif '0' not in str(i):
                for d in str(i):
                    if i%int(d):
                        isSelfDividing = False
                        break
                if isSelfDividing:
                    ans.append(i)

                isSelfDividing = True
        return ans           