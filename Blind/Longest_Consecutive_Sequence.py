from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        nums_set = set(nums)
        longest_sequesce = 1

        for num in nums_set:
            current_sequesnce = 1
            current_num = num
            while current_num + 1 in nums_set:
                current_sequesnce += 1
                current_num += 1 
            longest_sequesce = max(longest_sequesce, current_sequesnce)

        return longest_sequesce


nums = [100,4,200,1,3,2]

solution = Solution()

print(solution.longestConsecutive(nums))