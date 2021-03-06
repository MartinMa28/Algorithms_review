class NumMatrix:

    def __init__(self, matrix: list):
        if not matrix or not matrix[0]:
            self.pre_sum = None
        else:
            self.pre_sum = [[0 for _ in range(len(matrix[0]) + 1)] \
                            for _ in range(len(matrix)  + 1)]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    self.pre_sum[i + 1][j + 1] = self.pre_sum[i][j + 1] + \
                                                self.pre_sum[i + 1][j] - \
                                                self.pre_sum[i][j] + \
                                                matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.pre_sum:
            return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] -\
                    self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]
        else:
            return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)