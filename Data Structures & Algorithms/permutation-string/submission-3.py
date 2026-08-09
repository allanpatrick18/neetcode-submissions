class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        stack = list(s1)
        l =  0
        for r in range(len(s2)):

            while l < len(s2) and s2[l] in stack:
                stack.remove(s2[l])
                l = l + 1
                if len(stack) == 0:
                    return True
            
            stack = list(s1)
            l = r + 1
        
        return False
            