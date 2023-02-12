from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            parts = email.split("@")
            filtered = parts[0].split("+")
            local = filtered[0].split(".")
            email = "".join(local) + "@" + parts[1]
            unique.add(email)
        return len(unique)
