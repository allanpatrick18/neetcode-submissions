class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area_max = 0
        # for i in range(0, len(heights)):
        #     for j in range (i + 1, len(heights)):
        #         base = abs(i - j)
        #         area = base * min(heights[i],heights[j])
        #         if area > area_max:
        #             area_max = area

        # return area_max

        l = 0
        r = len(heights) -1
        area_max = 0
        while l < r:
            base = abs(r - l)
            area = base * min(heights[l],heights[r])
            area_max = max(area, area_max)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r -=1

        return area_max
        