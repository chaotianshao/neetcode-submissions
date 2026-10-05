class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # make nums1 the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1)

        while left <= right:

            mid = left + (right - left) // 2

            partition1 = mid
            partition2 = (len(nums1) + len(nums2) + 1) // 2 - partition1

            # four boundary values
            left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
            right1 = float("inf") if partition1 == len(nums1) else nums1[partition1]

            left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
            right2 = float("inf") if partition2 == len(nums2) else nums2[partition2]

            # correct partition
            if left1 <= right2 and left2 <= right1:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)

            # too many elements from nums1 on the left
            elif left1 > right2:
                right = mid - 1

            # too few elements from nums1 on the left
            else:
                left = mid + 1