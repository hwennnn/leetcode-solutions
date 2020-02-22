class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            local_name,domain_name = email.split("@")
            local_name ="".join(local_name.split('+')[0].split('.'))
            email = local_name +'@' + domain_name
            email_set.add(email)
        return len(email_set)