class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            elif token == "*":
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            else:
                stack.append(int(token))
        
        return stack[0]