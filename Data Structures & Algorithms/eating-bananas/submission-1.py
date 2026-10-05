class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range: from minimum speed (1) to maximum speed (max pile)
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            time = 0
            
            # Calculate total hours needed at speed 'mid'
            for pile in piles:
                time += math.ceil(pile / mid)
            
            # If Koko can finish within h hours, 'mid' is a valid speed.
            # Try to find a smaller valid speed by moving left.
            if time <= h:
                right = mid
            # If Koko takes too long, 'mid' is too slow. Increase the speed.
            else:
                left = mid + 1
        
        return left