class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        right = 0
        sub = []

        while right < len(s):
            if s[right] not in sub:
                sub.append(s[right])
                right += 1
                res = max(len(sub), res)
            else:
                res = max(len(sub), res)
                left += 1
                sub = sub[1:]
        return res
