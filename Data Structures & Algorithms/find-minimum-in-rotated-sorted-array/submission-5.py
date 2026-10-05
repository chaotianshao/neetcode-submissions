class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # We use left < right because we want the loop to stop 
        # when left == right, pointing directly at the minimum element.
        while left < right:
            mid = left + (right - left) // 2

            # If mid element is greater than the rightmost element,
            # the minimum must be in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is in the left half (including mid).
            else:
                right = mid
        
        # When left == right, we've converged on the minimum.
        return nums[left]