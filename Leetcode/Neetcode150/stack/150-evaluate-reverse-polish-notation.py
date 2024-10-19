class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-/*":
                a, b = stack.pop(), stack.pop()
                match token:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(b - a)
                    case "/":
                        stack.append(int(b / a))
                    case "*":
                        stack.append(a * b)
            else:
                stack.append(int(token))
        
        return stack[-1]