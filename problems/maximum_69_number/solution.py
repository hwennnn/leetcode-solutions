class Solution:
    def maximum69Number (self, num: int) -> int:
        

        lst = [i for i in str(num)]

        for i in range(len(lst)):
            if lst[i] == "6":
                lst[i] = "9"
                return (int("".join(lst)))
            
        return (int("".join(lst)))
