class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = float('inf')

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                # nums[mid] could be the minimum
                ans = min(ans, nums[mid])

                # Look for an even smaller one
                right = mid - 1
            else:
                # Minimum must be to the right
                left = mid + 1

        return ans