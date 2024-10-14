class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            '}': '{',
            ')': '(',
            ']': '['
        }
    
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack or brackets[c] != stack.pop():
                    return False

        return len(stack) == 0
            

