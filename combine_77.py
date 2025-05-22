class Solution:
    n = 4
    k = 2
    def combine(self, n: int, k: int) -> list[list[int]]:

        result = []

        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return result


# backtrack(1, [])
# ├── i=1 → path = [1]
# │   └── backtrack(2, [1])
# │       ├── i=2 → path = [1,2] ✅
# │       ├── i=3 → path = [1,3] ✅
# │       └── i=4 → path = [1,4] ✅
# ├── i=2 → path = [2]
# │   └── backtrack(3, [2])
# │       ├── i=3 → path = [2,3] ✅
# │       └── i=4 → path = [2,4] ✅
# ├── i=3 → path = [3]
# │   └── backtrack(4, [3])
# │       └── i=4 → path = [3,4] ✅
# └── i=4 → path = [4]
#     └── backtrack(5, [4]) → বাতিল (কারণ path এর size < k)
