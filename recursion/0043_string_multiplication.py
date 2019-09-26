class Solution:
    def _equalize_length(self, *args) -> tuple:
        max_len = max(map(len, args))

        return tuple(map(lambda x: x.zfill(max_len), args))


    def _add(self, *args) -> str:
        return str(sum(map(int, args)))


    def _sub(self, num1: str, num2: str) -> str:
        return str(int(num1) - int(num2))


    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = self._equalize_length(num1, num2)
        n = len(num1)

        if n == 1:
            # multiply by single digit
            return str(int(num1) * int(num2))

        num1_h = num1[: n // 2]
        num1_l = num1[n // 2:]
        num2_h = num2[: n // 2]
        num2_l = num2[n // 2:]

        num1_h_num2_h = self.multiply(num1_h, num2_h)
        num1_l_num2_l = self.multiply(num1_l, num2_l)
        combo = self._sub(self.multiply(self._add(num1_h, num1_l), self._add(num2_h, num2_l)), self._add(num1_h_num2_h, num1_l_num2_l))

        return self._add(num1_h_num2_h + '0' * 2 * (n - n // 2), combo + '0' * (n - n // 2), num1_l_num2_l)




if __name__ == "__main__":
    solu = Solution()

    print(solu.multiply('123', '456'))