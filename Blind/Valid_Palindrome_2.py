s = "A man, a plan, a canal: Panama"
# True
# s = "race a car"
# False

class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            # print(s[l])
            # print(s[r])            
            l += 1
            r -= 1
        return True
        


print(Solution().isPalindrome(s))