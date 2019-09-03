class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        cache = {}
        for idx, r in enumerate(list1):
            cache[r] = idx + 1

        least = len(list1) + len(list2)
        common = []
        for idx, r in enumerate(list2):
            if cache.get(r):
                if (cache.get(r) + idx + 1) == least:
                    common.append(r)
                elif (cache.get(r) + idx + 1) < least:
                    common = [r]
                    least = (cache.get(r) + idx + 1)

        return common


if __name__ == "__main__":
    solu = Solution()
    print(solu.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))