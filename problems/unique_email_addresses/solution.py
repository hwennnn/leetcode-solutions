class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        
        for email in emails:
            prefix, domain = email.split('@')
            prefix = prefix.split('+')[0]
            res.add("".join(e for e in prefix if e != '.') + "@" + domain)
        
        return len(res)