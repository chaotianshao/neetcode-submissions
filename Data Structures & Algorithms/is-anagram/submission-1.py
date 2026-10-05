class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        for char in s:
            sHash[char] = sHash.get(char,0) + 1
        
        for char in t:
            if char in sHash:
                sHash[char] = sHash[char] - 1
                if sHash[char] == 0:
                    del sHash[char]
            else:
                return False
        
        if len(sHash) == 0:
            return True
        else:
            return False