from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()

        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
            
        sorted_k_by_v = []
        for key, value in hash_map.items():
            sorted_k_by_v.append([value, key])
        sorted_k_by_v.sort()
            
        result = []
        while k:
            result.append(sorted_k_by_v.pop()[1])
            k -= 1
        return result
