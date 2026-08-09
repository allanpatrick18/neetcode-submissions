class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for idx, ele in enumerate(temperatures):
            while stack and ele > stack[-1][0]:
                t , i = stack.pop()
                res[i] = idx - i
                
            stack.append((ele, idx))

        return res   
            
