List = [2, 4, 5, 6]
target = 6


class Solution:
    def twosums(self, nums, target):
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return (prevMap[diff], i)
            prevMap[n] = i


print(Solution().twosums(List, target))
