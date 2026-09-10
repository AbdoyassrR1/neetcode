from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        hash_map = {}
        sequence = []
        i = 0
        j = 1
        while i < len(nums) - 1:
            if nums[j] - nums[i] == 1:
                sequence.append(nums[i])
                if i == len(nums) - 2:
                    sequence.append(nums[j])
                    hash_map[sequence[0]] = len(sequence)
            else:
                sequence.append(nums[i])
                hash_map[sequence[0]] = len(sequence)
                sequence.clear()
            
            i += 1
            j += 1
        return max(hash_map.values()) if hash_map else 1