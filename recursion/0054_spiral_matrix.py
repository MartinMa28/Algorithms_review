class Solution:
    @staticmethod
    def _size_of_matrix(matrix):
        return len(matrix), len(matrix[0])
    
    def spiralOrder(self, matrix: list) -> list:
        res = []
        
        def _spiral(matrix):
            if not matrix:
                return
            
            m, n = self._size_of_matrix(matrix)
            if min((m, n)) == 0:
                return
            elif min((m, n)) == 1:
                if m == 1:
                    # one row
                    res.extend(matrix[0])
                else:
                    # one column
                    res.extend([row[0] for row in matrix])
            else:
                # add the first row
                res.extend(matrix[0])
                
                # add the column on the right boundary
                res.extend([row[-1] for row in matrix[1:]])
                
                # add the last row
                res.extend(matrix[-1][-2::-1])
                
                # add the column on the left boundary
                res.extend([row[0] for row in matrix[-2:0:-1]])
                
                _spiral([row[1: -1] for row in matrix[1: -1]])
                
        _spiral(matrix)
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))