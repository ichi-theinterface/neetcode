
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    s_list = []
    t_list = []
    for letter in s:
        s_list.append(letter)
    for letter in t:
        t_list.append(letter)
    s_list.sort()
    t_list.sort()
    if s_list == t_list:
        return True
    else:
        return False

print(isAnagram("aa", "a"))
