from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counter_s = dict()

        for i in range(len(strs)):
            s = tuple(sorted(strs[i]))
            if s in counter_s.keys():
                counter_s[s].append(strs[i])
            else:
                counter_s[s] = [strs[i]]
        return [val for val in counter_s.values()]



strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))