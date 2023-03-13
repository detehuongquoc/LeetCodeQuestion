# Using Monotonic stack decrease
# check if greater from stack, we pop and add it into index of array
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, v in enumerate(temperatures):

            while stack and v > temperatures[stack[-1]]:
                newValue = stack.pop()
                result[newValue] = i - newValue

            stack.append(i)

        return result
