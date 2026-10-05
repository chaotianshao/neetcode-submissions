class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = defaultdict(int)

        if len(s1) > len(s2):
            return False

        l, r = 0, 0
        
        for char in s1:
            mp[char] += 1

        mp1 = mp.copy()
        while r < len(s2):
            print(f'{r}, {s2[r]}, {mp1[s2[r]]}' )
           
            if mp1[s2[r]] > 0:
                mp1[s2[r]] -= 1
                r += 1
            else:
                l += 1
                r = l
                mp1 = mp.copy()
            
            if sum(mp1.values()) == 0:
                return True

        return False

            
