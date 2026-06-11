class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        lMax, rMax = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                lMax = max(lMax, height[left])
                res += lMax - height[left]
                left += 1
            else:
                rMax = max(rMax, height[right])
                res += rMax - height[right]
                right -= 1

        return res