
def containsDuplicate(nums):
   """
   :type nums: List[int]
   :rtype: bool
   """
   l = len(nums)
   nums.sort()
   for i in range(0, l-1):
       if nums[i] == nums[i+1]:
           return True
   return False

nums = [1, 2, 3, 4, 1]
print(containsDuplicate(nums))