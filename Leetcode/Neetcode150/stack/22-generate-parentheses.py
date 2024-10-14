class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def generate(open_count, closed_count):
            if len(stack) == 2 * n:
                res.append("".join(stack))
                return

            if open_count < n:
                stack.append("(")
                generate(open_count + 1, closed_count)
                stack.pop()

            if open_count > closed_count:
                stack.append(")")
                generate(open_count, closed_count + 1)
                stack.pop()
        
        generate(0, 0)
        return res
