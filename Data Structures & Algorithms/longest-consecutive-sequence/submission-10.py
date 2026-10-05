class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        startNum = []

        for num in nums:
            if num - 1 not in myset:
                startNum.append(num)
        
        res = 0
        for num in startNum:
            maxLen = 1
            tmp = num
            while tmp + 1 in myset:
                maxLen += 1
                tmp += 1
            
            if maxLen > res:
                res = maxLen
        
        return res
