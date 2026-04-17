class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        for letter in s:
            hs[letter] = hs.get(letter, 0) + 1
        for letter in t:
            if letter not in hs or hs.get(letter) == 0:
                return False
            hs[letter] -= 1
        return True

            
        