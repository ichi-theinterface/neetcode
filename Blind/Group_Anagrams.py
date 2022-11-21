strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Expected_Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs):

        get_num = []
        for str in strs:
            get_num.append(sorted(str))

        new_get_num = []
        for i in get_num:
            if i not in new_get_num:
                new_get_num.append(i)
        # new_get_num = [['a', 'e', 't'], ['a', 'n', 't'], ['a', 'b', 't']]

        output = []
        len_of_output = len(new_get_num)
        while len_of_output > 0:
            output.append([])
            len_of_output -= 1
        # output = [[], [], []]

        for i in output:
            for str in strs:
                sorted(str) == 
            # print(i)
        
        return new_get_num
        


print(Solution().groupAnagrams(strs))
