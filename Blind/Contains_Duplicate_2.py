
nums = [1, 2, 3, 4, 1]
# nums = [1, 2, 3, 4]

class Solution:
    def containsDuplicate(self, nums):
        a = []
        for b in nums:
            if b in a:
                return True
            a.append(b)
        return False


print(Solution().containsDuplicate(nums))