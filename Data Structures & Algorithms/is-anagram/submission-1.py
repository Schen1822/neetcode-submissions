class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = {}
        for c in s:
            chars.setdefault(c, 0)
            chars[c] = chars[c]+1
        for c in t:
            if c not in chars.keys():
                return False
            else:
                chars[c] = chars[c]-1
        for c in chars.keys():
            if chars[c] != 0:
                return False
        return True
        