class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in hashMap:
                hashMap[sortedS].append(s)
            else:
                hashMap[sortedS] = [s]
        result = []
        for val in hashMap:
            result.append(hashMap[val])
        
        return result
