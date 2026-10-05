class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Limit Exceeded
        # res = 0
        # for i in range(len(s)):
        #     hashMap = {}
        #     tmp = 0
        #     for j in range(i, len(s)):
        #         if s[j] not in hashMap:
        #             tmp += 1
        #             hashMap[s[j]] = 1
        #         else:
        #             break
        #     # print(hashMap)
        #     res = max(tmp, res)

        # return res
        
        if len(s) == 0:
            return 0

        left = 0
        right = 1
        hash_map = {}
        hash_map[s[left]] = 1
        res = 1 
        tmp = 1
        while right < len(s):
            # print(s[right])
            if s[right] not in hash_map:
                hash_map[s[right]] = 1
                right += 1
                tmp += 1
            else:
                while s[right] in hash_map:
                    # print(hash_map)
                    del hash_map[s[left]]
                    # print(hash_map)
                    left += 1
                tmp = right - left + 1
                hash_map[s[right]] = 1
                right += 1
            res = max(res, tmp)
        
        return res



