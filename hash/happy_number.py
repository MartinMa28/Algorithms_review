class Solution:
    def _split_digits(self, n: int) -> list:
        digits = []
        while n >= 10:
            digits.append(n % 10)
            n //= 10

        digits.append(n)
        return digits

    def isHappy(self, n: int) -> bool:
        cache = set()

        while n not in cache:
            cache.add(n)
            digits = self._split_digits(n)
            square_sum = sum(map(lambda x: x**2, digits))
            if square_sum == 1:
                return True
                
            n = square_sum

        return False


if __name__ == "__main__":
    solu = Solution()
    print(solu.isHappy(19))
