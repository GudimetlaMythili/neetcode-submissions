class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if length of s and t are the same -> false if not
        if len(s) != len(t):
            return False
        # hashmap - key: letter, value: freq
        countS, countT = {}, {}

        for c in range(len(s)):
            countS[s[c]] = 1 + countS.get(s[c], 0)
            countT[t[c]] = 1 + countT.get(t[c], 0)
        
        return countS == countT