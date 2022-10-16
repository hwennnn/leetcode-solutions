class Solution:
    def maskPII(self, s: str) -> str:
        a = s.find("@")
        
        if a != -1:
            return (s[0] + "*" * 5 + s[a - 1:]).lower()
        
        digits = "".join([x for x in s if x.isdigit()])

        return ["", "+*-", "+**-", "+***-"][len(digits) - 10] + "***-***-" + digits[-4:]