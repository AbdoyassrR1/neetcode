from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexs = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                com_index = nums.index(complement)
                if i != com_index:
                    return sorted([i, com_index])
        
        return []