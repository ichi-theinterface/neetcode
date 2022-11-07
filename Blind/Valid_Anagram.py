
# def isAnagram(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     s_list = []
#     t_list = []
#     for letter in s:
#         s_list.append(letter)
#     for letter in t:
#         t_list.append(letter)
#     s_list.sort()
#     t_list.sort()
#     if s_list == t_list:
#         return True
#     else:
#         return False



"""
Solution from neetcomde.io

dictionary.get(keyname, value)
keyname	(Required): The keyname of the item you want to return the value from
value	(Optional): A value to return if the specified key does not exist.Default value None

console log
{'a': 3, 'c': 1, 'd': 1, 'o': 1, 'n': 2}
{'a': 3, 'c': 1, 'd': 1, 'o': 1, 'n': 2}
True
"""
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    print(countS)
    print(countT)
    return countS == countT

print(isAnagram("anaconda", "aanconad"))
