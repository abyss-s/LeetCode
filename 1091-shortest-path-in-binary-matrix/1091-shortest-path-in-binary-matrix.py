from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # 시작점, 끝점이 막혀있다면 연결 불가
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        dx = [1, 1, 1, -1, -1, -1, 0, 0]
        dy = [0, 1, -1, 0, 1, -1, 1, -1]

        visited = set()
        q = deque([(0, 0, 1)])

        while q:
            x, y, cur = q.popleft()

            if grid[x][y] == 1:
                continue
            if (x, y) in visited:
                continue
            if (x, y) == (n - 1, n - 1):
                return cur

            visited.add((x, y))

            for i in range(8):
                ax, ay = x + dx[i], y + dy[i]
                if 0 <= ax < n and 0 <= ay < n:
                    q.append((ax, ay, cur + 1))

        return -1
