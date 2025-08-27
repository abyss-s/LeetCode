class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        res = [0] * n
        for i, target in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < target:
                j = stk.pop()
                res[j] = i - j
            stk.append(i)
        return res