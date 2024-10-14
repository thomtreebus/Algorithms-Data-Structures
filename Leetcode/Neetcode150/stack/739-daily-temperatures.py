class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # [temp, index]

        for index in range(len(temperatures)):
            while stack and temperatures[index] > stack[-1][0]:
                temp, i = stack.pop()
                answer[i] = index - i
            
            stack.append([temperatures[index], index])

        return answer
