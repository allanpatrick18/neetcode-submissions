import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = [r]
        while l <= r:
            m = (r + l) // 2
            tot = 0
            for p in piles:
                tot += math.ceil(p / m)
            
            if tot > h:
               l = m + 1
            if tot <= h:
               r = m - 1
               res.append(m)

    
        return min(res)
        
            



