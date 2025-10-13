class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        def dfs(node, c):
            color[node] = c
            for nxt in graph[node]:
                # 같은 색이면 실패
                if color[nxt] == c:
                    return False
                if color[nxt] == 0 and not dfs(nxt, -c):
                    return False
            return True

        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True