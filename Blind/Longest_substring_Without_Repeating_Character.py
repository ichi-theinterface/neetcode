class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_substring = 0
        left, right = 0, 0
        stringset = set()

        while left < len(s) and right < len(s):
            if s[right] not in stringset:
                print(f"moving right, {s[right]}")
                stringset.add(s[right])
                right +=1
                len_substring = max(len_substring, right - left)
            else:
                print(f"moving left, {s[left]}")
                stringset.remove(s[left])
                left += 1
        return len_substring

solution = Solution()

s = "pwwkew"

print(solution.lengthOfLongestSubstring(s=s))

