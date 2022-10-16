class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        
        for email in emails:
            email, provider = email.split("@")
            curr = ""
            
            for x in email:
                if x == ".": continue
                if x == "+": break
                
                curr += x
            
            s.add(curr + "@" + provider)
        
        return len(s)