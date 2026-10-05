class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for idx in range(len(nums)):
            hm = {}
            target = nums[idx]
            for x in range(idx+1, len(nums)):
                if -(nums[x]+target) in hm:
                    tmp = sorted([target, nums[x], -(nums[x]+target)])
                    if tmp not in res:
                        res.append(tmp)
                else:
                    hm[nums[x]] = 1

        return res 

