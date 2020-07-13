class Solution(object):
    def trap(self, height):
        if len(height) < 3 or not height:
            return 0

        totalRain = 0
        left, right = 0, len(height)-1
        lMax, rMax = height[left], height[right]
        while left < right:
            if lMax <= rMax:
                totalRain += lMax - height[left]
                left += 1
                lMax = max(lMax, height[left])
            else:
                totalRain += rMax - height[right]
                right -= 1
                rMax = max(rMax, height[left])

        return totalRain


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
