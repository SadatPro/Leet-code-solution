class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        x = 0
        for op in operations:
            if "++" in op:
                x += 1
            else:
                x -= 1
        return x

operations = ["x++", "x++"]
sol = Solution()
result = sol.finalValueAfterOperations(operations)
print(result)  # এই লাইনটা না থাকলে কিছুই দেখাবে না
