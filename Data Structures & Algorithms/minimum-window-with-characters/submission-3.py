class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = defaultdict(int)
        if len(s) < len(t):
            return ""

        for char in t:
            mp1[char] += 1
        
        l = 0
        r = 0

        res = []
        while l < len(s):
            while l < len(s) and s[l] not in mp1:
                l += 1
            
            r = l
            mp2 = defaultdict(int)
            tmp_res = []
            while r < len(s):
                if s[r] in mp1:
                    if mp2[s[r]] < mp1[s[r]]:
                        mp2[s[r]] += 1
                tmp_res.append(s[r])

                if mp2 == mp1:
                    res.append(tmp_res)
                    break
                
                r += 1
            
            l += 1

        if len(res) == 0:
            return ""
        
        minIdx = 0
        minLen = len(res[0])
        for idx in range(len(res)):
            if len(res[idx]) < minLen:
                minIdx = idx
                minLen = len(res[idx])
        
        return "".join(res[minIdx])


