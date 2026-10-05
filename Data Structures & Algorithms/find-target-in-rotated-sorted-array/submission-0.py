class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        print(left)
        if target < nums[left]:
            return -1 
        elif target <= nums[-1]:
            right = len(nums) - 1
        elif target >= nums[0]:
            right = left - 1
            left = 0
        
        while left <= right:
            mid = left + (right - left ) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
