class Solution:
    def __init__(self):
        self.directions = [[1, 0, True], [-1, 0, True], [0, 1, True], [0, -1, True],
                            [1, 1, True], [-1, -1, True], [1, -1, True], [-1, 1, True]]
        self.attack_list = []


    @classmethod
    def _is_safe(cls, i, j):
        return i >= 0 and i < 8 and j >= 0 and j < 8


    def _bfs(self, king, step=1):
        k_i, k_j = king
        for d in self.directions:
            if d[2]:
                next_i, next_j = (k_i + d[0] * step, k_j + d[1] * step)
                if Solution._is_safe(next_i, next_j):
                    if self.board[next_i][next_j] == 'Q':
                        self.attack_list.append([next_i, next_j])
                        d[2] = False
                else:
                    d[2] = False
        
        if sum([d[2] for d in self.directions]) == 0:
            return
        else:
            self._bfs(king, step + 1)
                

    def queensAttacktheKing(self, queens: list, king: list) -> list:
        self.board = [['N' for _ in range(8)] for _ in range(8)]
        for q in queens:
            self.board[q[0]][q[1]] = 'Q'

        self.board[king[0]][king[1]] = 'K'

        self._bfs(king)

        return self.attack_list


if __name__ == "__main__":
    solu = Solution()
    print(solu.queensAttacktheKing([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]))
        