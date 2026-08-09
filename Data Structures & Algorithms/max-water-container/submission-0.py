class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_max = 0
        for i in range(0, len(heights)):
            for j in range (i + 1, len(heights)):
                base = abs(i - j)
                area = base * min(heights[i],heights[j])
                if area > area_max:
                    area_max = area
                

        return area_max