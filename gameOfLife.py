# Time Complexity :
- O(m * n), where m is the number of rows and n is the number of columns

# Space Complexity :
- O(1), in-place updates using bit manipulation

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def countLiveNeighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),         (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    count += board[nr][nc] & 1  # only the current state
            return count
        
        for r in range(rows):
            for c in range(cols):
                live_neighbors = countLiveNeighbors(r, c)
                if board[r][c] == 1:
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[r][c] = 3  # 1 -> 1
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2  # 0 -> 1

        for r in range(rows):
            for c in range(cols):
                board[r][c] >>= 1  # Update to the next state
