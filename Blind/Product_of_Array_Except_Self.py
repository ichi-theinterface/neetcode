from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        return_array = []

        nums_len = len(nums)
        i = 0
        while i < nums_len:
            append_num = 1
            for k in range(nums_len):
                if k != i:
                    append_num = append_num * nums[k]

            return_array.append(append_num)
                    
            i += 1

        return return_array


nums = [1,2,3,4]

solution = Solution()

print(solution.productExceptSelf(nums))