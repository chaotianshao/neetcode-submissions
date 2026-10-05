class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for val in strs:
            sortedStr = "".join(sorted(val))
            if sortedStr in hashMap:
                hashMap[sortedStr].append(val)
            else:
                hashMap[sortedStr] = [val]

        res = []
        for val in hashMap:
            res.append(hashMap[val])
        return res                