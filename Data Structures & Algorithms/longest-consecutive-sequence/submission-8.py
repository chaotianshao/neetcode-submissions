class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0
        for num in numSet:
            length = 0
            if (num - 1) not in numSet:
               curr = num
               length = 1 
               while (curr + length) in numSet:
                length = length + 1
            res = max(res, length)
        
        return res

        