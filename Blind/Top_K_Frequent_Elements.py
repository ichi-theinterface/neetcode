nums = [3,3,3,4,4,5]
k = 2

class Solution:
    def opKFrequent(self, nums, k):
        frequency = []
        for num in nums:
            count = 0 
            for a in nums:
                if a == num:
                    count += 1
            frequency.append(count)
        for f in frequency:
            if f in frequency:
                frequency.remove(f)
        frequency

        return frequency


print(Solution().opKFrequent(nums, k))