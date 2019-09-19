class Solution:
    def __init__(self):
        self.spiral = []

    def _get_outer(self, matrix: list) -> list:
        if matrix == []:
            return

        spiral = []
        
        spiral.extend(matrix[0])
        
        spiral.extend([row[-1] for row in matrix[1:]])
        
        if len(matrix) > 1:
            spiral.extend(list(reversed(matrix[-1]))[1:])
        
        if len(matrix[0]) > 1:
            spiral.extend([row[0] for row in matrix[-2: 0: -1]])

        self.spiral.extend(spiral)
        self._get_outer([row[1: -1] for row in matrix[1: -1] if row[1: -1] != []])

    
    def spiralOrder(self, matrix: list) -> list:
        self._get_outer(matrix)
        res = self.spiral
        self.spiral = []

        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))