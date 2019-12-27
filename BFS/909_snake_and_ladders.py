from collections import deque

class Solution:
    def snakesAndLadders(self, board: list) -> tuple:
        idx_to_pos = {}
        idx = 1
        left_to_right = True
        n = len(board)
        
        cur_pos = (n - 1, 0)
        while idx <= n ** 2:
            if idx % n != 0:
                idx_to_pos[idx] = cur_pos
                if left_to_right:
                    cur_pos = (cur_pos[0], cur_pos[1] + 1)
                    idx += 1
                else:
                    cur_pos = (cur_pos[0], cur_pos[1] - 1)
                    idx += 1   
            else:
                idx_to_pos[idx] = cur_pos
                cur_pos = (cur_pos[0] - 1, cur_pos[1])
                left_to_right = left_to_right ^ True 
                idx += 1
                
        queue = deque([(1, 0)])
        visited = set([1])
        
        while queue:
            cur_idx, step = queue.popleft()
            if cur_idx == n ** 2:
                return step
            
            for i in range(1, 7):
                next_idx = cur_idx + i
                if next_idx <= n ** 2:
                    row, col = idx_to_pos[cur_idx + i]
                    if board[row][col] != -1:
                        next_idx = board[row][col]

                    if next_idx not in visited:
                        queue.append((next_idx, step + 1))
                        visited.add(next_idx)
        
        return -1