# s = "A man, a plan, a canal: Panama"
# True
s = "race a car"
# False

class Solution:
    def isPalindrome(self, s):
        lower_s = s.lower()
        new_s = ''.join(c for c in lower_s if c.isalnum())
        rev_s = new_s[::-1]
        if rev_s == new_s:
            return True
        else:
            return False
        


print(Solution().isPalindrome(s))