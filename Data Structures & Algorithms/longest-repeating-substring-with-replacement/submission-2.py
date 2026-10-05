class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        left, right = 0, 0
        res = 0
        max_freq = 0
        while right < len(s):
            mp[s[right]] = mp.get(s[right], 0) + 1
            max_freq = max(max_freq, mp[s[right]])
            
            if (right - left + 1) - max_freq > k:
                mp[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        
        return res