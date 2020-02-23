class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        diff = [i for i in arr1 if i not in arr2]
        diff.sort()

        dic = collections.Counter(arr1)

        temp = []

        for i in arr2:
            if i not in diff:
                for x in range(dic[i]):
                    temp.append(i)
                
        return temp + diff