class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
        for ele in s:
            if ele  == '[':
                stack.append(']')
            elif ele  == '(':
                stack.append(')')
            elif ele  == '{':
                stack.append('}')
            elif len(stack) > 0 and ele == stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
        