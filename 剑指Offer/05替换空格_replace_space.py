# Replace the space " " in one string to "%20"
# Input：s = "We are happy."
# Output："We%20are%20happy."
# Tip: Use library function.

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ','%20')
