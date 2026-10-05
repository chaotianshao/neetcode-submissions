class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = [0 for i in range(len(nums))]
        for idx in range(len(nums)):
            if idx == 0:
                prefix.append(1)
            else:
                prefix.append(nums[idx - 1] * prefix[-1])
        
        for idx in range(len(nums) -1 , -1, -1):
            if idx == len(nums) - 1:
                suffix[idx] = 1
            else:
                suffix[idx] = nums[idx+1] * suffix[idx+1]

        res = []
        for idx in range(len(nums)):
            res.append(prefix[idx] * suffix[idx])
        
        return res
