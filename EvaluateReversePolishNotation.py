# 150. Evaluate Reverse Polish Notation
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Declaring empty stack
        stack = []

        for token in tokens:
            if token == '+':
                # Can use below line and dont use separate variable
                stack.append(stack.pop() + stack.pop())

            elif token == '-':
                b = stack.pop() # First element popped from stack
                a = stack.pop() # Second element popped from stack
                stack.append(a-b)

            elif token == '*':
                b,a = stack.pop(), stack.pop()
                stack.append(a*b)

            elif token == '/':
               b,a = stack.pop(), stack.pop()
               # Type Conversion to int to avoid decimal value
               stack.append(int(a/b))

            elif token == '^':
                b,a = stack.pop(), stack.pop()
                stack.append(a**b)
            
            # else block for operands
            else:
                stack.append(int(token))
            
        return stack.pop()
                
                