# class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     left = 0
    #     right = len(nums) - 1

    #     while left <= right:
    #         mid = left + (right - left) // 2

    #         if nums[mid] > nums[right] and target < nums[right]:
    #             left = mid + 1
    #         elif nums[mid] > nums[right] and target > nums[right]:
    #             right = mid - 1
    #         elif nums[mid] < nums[right] and target < nums[mid]:
    #             left = mid + 1
    #         elif nums[mid] < nums[right] and target > nums[mid]:
    #             right = mid - 1
    #         elif nums[mid] < nums[right] and target == nums[mid]:
    #             return mid

    #         print(f'{left} {right}')
        
    #     return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


