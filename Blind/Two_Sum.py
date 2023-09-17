from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            k = i + 1
            while k < len(nums):
                if nums[i] + nums[k] == target:
                    return [i, k]
                k += 1
            i += 1 


solution = Solution()

nums = [2,5,5,11]
target = 10

print(solution.twoSum(nums, target))