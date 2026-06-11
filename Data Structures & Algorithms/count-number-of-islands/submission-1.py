
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid: return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         islands = 0
      
        

#         def bfs(row,col):
#             q = collections.deque()
#             q.append((row,col))
#             directions = [[0,1],[1,0],[-1,0],[0,-1]]
#             # visit.add((row,col))
#             grid[row][col] = 0
#             while q:
#                 r,c=q.popleft()
#                 for d in directions:
#                     new_r, new_c = r+d[0], c+d[1]
#                     if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r,new_c) not in visit:
#                         q.append((new_r,new_c))
#                         visit.add((new_r,new_c))

#         for r in range(rows):
#             for c in range(cols):
#                 curr = grid[r][c]
#                 if curr == "1" and (r,c) not in visit:
#                     bfs(r,c)
#                     islands += 1

#         return islands



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        #visit = set()
        islands = 0
      
        

        def bfs(row,col):
            q = collections.deque()
            q.append((row,col))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            # visit.add((row,col))
            grid[row][col] = 0
            while q:
                r,c=q.popleft()
                for d in directions:
                    new_r, new_c = r+d[0], c+d[1]
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1":
                        q.append((new_r,new_c))
                        grid[new_r][new_c]=0

        for r in range(rows):
            for c in range(cols):
                curr = grid[r][c]
                if curr == "1":
                    bfs(r,c)
                    islands += 1

        return islands
