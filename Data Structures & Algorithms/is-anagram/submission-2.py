class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        for char in s:
            hash_map[char] = hash_map.get(char,0) + 1
        
        for char in t:
            if char in hash_map and hash_map[char] > 0:
                hash_map[char] = hash_map[char] - 1
            else:
                return False
        
        for char in hash_map:
            if hash_map[char] != 0:
                return False
        
        return True