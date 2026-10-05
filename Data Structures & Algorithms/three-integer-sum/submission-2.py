class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            hashmap = {}
            target = nums[i] * -1
            for j in range(len(nums)):
                if j != i:
                    if target - nums[j] in hashmap:
                        tmp = sorted([nums[i],nums[j],nums[hashmap[target-nums[j]]]])
                        if tmp not in res:
                            res.append(tmp)
                    else:
                        hashmap[nums[j]] = j
            
        return res