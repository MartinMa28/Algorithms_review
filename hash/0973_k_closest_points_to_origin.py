class Solution:
    def kClosest(self, points: list, K: int) -> list:
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:K]


if __name__ == "__main__":
    solu = Solution()
    print(solu.kClosest([[0,1],[1,0]], 2))