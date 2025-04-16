from collections import deque

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
def numislands(grid):

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))
            while queue:
                current_row, current_col = queue.popleft()
                for drow, dcolumn in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    new_row,new_column = current_row + drow, current_col + dcolumn
                    if(
                        0 <= new_row < rows and
                        0 <= new_column < cols and

                        grid[new_row][new_column] == "1" and
                        (new_row,new_column) not in visited
                    ):
                        queue.append((new_row, new_column))
                        visited.add((new_row, new_column))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1


        return islands

print("Number of islands:", numislands(grid))