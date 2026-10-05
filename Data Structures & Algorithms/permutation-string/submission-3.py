class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap = {}
        s1Len = len(s1)
        for s in s1:
            hashMap[s] = hashMap.get(s, 0) + 1
        
        # print(hashMap)

        left = 0
        for right in range(s1Len-1, len(s2)):
            hashMap2 = {}
            for i in range(left, right+1):
                hashMap2[s2[i]] = hashMap2.get(s2[i], 0) + 1

            # print(hashMap2)
            if hashMap == hashMap2:
                return True
            left += 1
        
        return False
        
