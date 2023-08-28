class Solution:
    # O(n) memory solution
    def trap(self, height: List[int]) -> int:
        water = 0
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        currentMax = 0
        for i in range(len(height)):
            maxLeft[i] = currentMax
            currentMax = max(height[i], currentMax)
        currentMax = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = currentMax
            currentMax = max(height[i], currentMax)
        
        for i in range(len(height)):
            water += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        
        return water