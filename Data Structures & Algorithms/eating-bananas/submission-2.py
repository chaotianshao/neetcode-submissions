class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1

        while left <= right:
            mid = left + (right - left) // 2

            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                # mid works!
                ans = mid

                # But maybe there is a smaller k that also works.
                right = mid - 1

            else:
                # mid is too slow.
                left = mid + 1

        return ans