class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftSide = [0] * len(height)
        rightSide = [0] * len(height)

        for i in range(1, len(height)):
            if i == 1:
                leftSide[i] = height[i-1]
            else:
                leftSide[i] = max(height[i-1], leftSide[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            if i == len(height) - 2:
                rightSide[i] = height[-1]
            else:
                rightSide[i] = max(height[i+1], rightSide[i+1])

        for i in range(len(height)):
            if leftSide[i] >= height[i] and rightSide[i] >=height[i]:
                res += min(leftSide[i], rightSide[i]) - height[i]

        return res    