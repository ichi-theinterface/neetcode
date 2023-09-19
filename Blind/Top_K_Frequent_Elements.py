from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            if num not in frequency_dict:
                frequency_dict[num] = 1
            else:
                frequency_dict[num] += 1
        sorted_dict = sorted(frequency_dict, key=frequency_dict.get, reverse=True)
        
        return_array = []
        i = 0
        while i < k:
            return_array.append(sorted_dict[i])
            i += 1
        return return_array


nums = [1,1,1,2,2,3,3,3]
k = 2

solution = Solution()

solution.topKFrequent(nums, k)
        
print(solution.topKFrequent(nums, k))    