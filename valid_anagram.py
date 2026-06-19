class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = dict()
        counter_t = dict()

        for i in range(len(s)):
            if s[i] in counter_s:
                counter_s[s[i]] = counter_s[s[i]] + 1
            else:
                counter_s[s[i]] = 1
            
            if t[i] in counter_t:
                counter_t[t[i]] = counter_t[t[i]] + 1
            else:
                counter_t[t[i]] = 1

        return counter_s == counter_t