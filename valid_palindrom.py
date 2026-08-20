class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_s = ""
        for c in s:
            if c.isalnum():
                alphanum_s += c.lower()
        
        return alphanum_s == alphanum_s[::-1]