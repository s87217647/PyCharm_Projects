from collections import deque
from typing import List


class NumbersOfIsland:
    # solve it using bfs
    def numIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        islandCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    islandCount += 1
                    self.bfs(i, j, grid)  # 我觉得这个X, Y 还有争议
        return islandCount

    def bfs(self, x, y, grid):
        queue = deque([(x, y)])
        grid[x][y] = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newX = x + dx
                    newY = y + dy
                    if newX not in range(len(grid)) or newY not in range(len(grid[0])):
                        continue

                    if grid[newX][newY] == 1:
                        grid[newX][newY] = 0
                        queue.append((newX, newY))

    def bfs2(self, x, y, grid):  # 自己重新默写一遍，看是否真的理解
        grid[x][y] = 0
        queue = deque([(x, y)])
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nX, nY = x + dx, y + dy

                    if nX not in range(len(grid)) or nY not in range(len(grid[0])):
                        continue

                    if grid[nX][nY] == 1:
                        queue.append((nX, nY))
                        grid[nX][nY] = 0

