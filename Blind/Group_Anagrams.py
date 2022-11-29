from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Expected_Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for l in s:
                count[(ord(l) - ord("a"))] += 1
            # print(count)
            result[tuple(count)].append(s)

        answer = []
        for res in result.values():
            answer.append(res)

        return answer


print(Solution().groupAnagrams(strs))
