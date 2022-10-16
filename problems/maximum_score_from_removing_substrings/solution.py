class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        def remove(s, target, val):
            st = []
            ret = 0
            for c in s:
                st.append(c)
                if len(st)>=2 and (st[-2],st[-1])==target:
                    st.pop()
                    st.pop()
                    ret+= val
            return st, ret
        if y > x:
            s, val1 = remove(s, ('b','a'), y)
            s, val2 = remove(s, ('a','b'), x)
            return val1+val2
        s, val1 = remove(s, ('a','b'), x)
        s, val2 = remove(s, ('b','a'), y)
        return val1+val2