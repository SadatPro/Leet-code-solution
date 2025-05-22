class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, end):
            if start == end:
                result.append(nums[:])
                return
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0, len(nums))
        return result


    # backtrack(0)
# ├── swap(0,0) → [1, 2, 3]
# │   └── backtrack(1)
# │       ├── swap(1,1) → [1, 2, 3]
# │       │   └── backtrack(2)
# │       │       ├── swap(2,2) → [1, 2, 3]
# │       │       │   └── backtrack(3) ✅ add [1, 2, 3]
# │       │       └── end loop (i=2 done)
# │       ├── swap(1,2) → [1, 3, 2]
# │       │   └── backtrack(2)
# │       │       ├── swap(2,2) → [1, 3, 2]
# │       │       │   └── backtrack(3) ✅ add [1, 3, 2]
# │       │       └── end loop
# │       └── end loop (i=1,2 done)
# │
# ├── swap(0,1) → [2, 1, 3]
# │   └── backtrack(1)
# │       ├── swap(1,1) → [2, 1, 3]
# │       │   └── backtrack(2)
# │       │       ├── swap(2,2) → [2, 1, 3]
# │       │       │   └── backtrack(3) ✅ add [2, 1, 3]
# │       │       └── end loop
# │       ├── swap(1,2) → [2, 3, 1]
# │       │   └── backtrack(2)
# │       │       ├── swap(2,2) → [2, 3, 1]
# │       │       │   └── backtrack(3) ✅ add [2, 3, 1]
# │       │       └── end loop
# │       └── end loop
# │
# └── swap(0,2) → [3, 2, 1]
#     └── backtrack(1)
#         ├── swap(1,1) → [3, 2, 1]
#         │   └── backtrack(2)
#         │       ├── swap(2,2) → [3, 2, 1]
#         │       │   └── backtrack(3) ✅ add [3, 2, 1]
#         │       └── end loop
#         ├── swap(1,2) → [3, 1, 2]
#         │   └── backtrack(2)
#         │       ├── swap(2,2) → [3, 1, 2]
#         │       │   └── backtrack(3) ✅ add [3, 1, 2]
#         │       └── end loop
#         └── end loop
