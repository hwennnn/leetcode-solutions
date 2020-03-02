class Solution:
    def isValid(self, s: str) -> bool:
        maps = {')':'(', '}':'{', ']':'['}
        st = []
        for e in s:
            if st and (e in maps and st[-1] == maps[e]):
                st.pop()
            else:
                st.append(e)
        return not st