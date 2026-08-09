class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        size = len(tokens)
        stack = []
        def operate_stack(operator):
           
            res = None
            print(stack)
            ele = stack.pop()
            res = stack.pop()
            if operator == '+':
                res  = ele + res
            if operator == '-':
                res = res - ele
            if operator == '*':
                res = ele * res
            if operator == '/':
                res = int(res / ele)

            
            stack.append(res)
            return stack
                
            
        for i in range(0, len(tokens)):

            try:
                n = float(tokens[i])
                stack.append(int(n))
            except:
               stack = operate_stack(tokens[i])
               
        
        return stack[0]

        # stack = []
        # for c in tokens:
        #     print(stack)
        #     if c == "+":
        #         stack.append(stack.pop() + stack.pop())
        #     elif c == "-":
        #         a, b = stack.pop(), stack.pop()
        #         stack.append(b - a)
        #     elif c == "*":
        #         stack.append(stack.pop() * stack.pop())
        #     elif c == "/":
        #         a, b = stack.pop(), stack.pop()
        #         print(a,b)
        #         stack.append(int(float(b) / a))
        #     else:
        #         stack.append(int(c))


        # return stack[0]


                
