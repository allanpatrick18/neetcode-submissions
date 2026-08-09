class Solution:
    def trap(self, height: List[int]) -> int:
        
        size = len(height)
        left = [0] * size
        right = [0] * size
        maxleft = 0
        maxright = 0
        for i in range(1, size):
            maxleft = max(maxleft,height[i - 1])
            left[i] = maxleft
            maxright = max(maxright,height[size -i])
            right[size -i -1] = maxright
        
        water = 0
        print(right)
        print(left)
        for i in range(1, size):
            water += max(min(left[i],right[i]) - height[i],0)

        return water

            
            
            