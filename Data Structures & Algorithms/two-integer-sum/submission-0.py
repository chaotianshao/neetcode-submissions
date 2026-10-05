class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            if target - num in seen:
                if idx > seen[target - num]:
                    return [seen[target - num], idx]
                else:
                    return [idx, seen[target - num]]
            else:
                seen[num] = idx
        