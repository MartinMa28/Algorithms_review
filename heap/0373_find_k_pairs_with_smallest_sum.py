import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        res = []
        seen = set()
        
        # element in heap: (sum, index_1, index_2)
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        
        while len(res) < k and min_heap:
            _, idx_1, idx_2 = heapq.heappop(min_heap)
            res.append([nums1[idx_1], nums2[idx_2]])

            if idx_1 + 1 < len(nums1) and (idx_1 + 1, idx_2) not in seen:
                heapq.heappush(min_heap, (nums1[idx_1 + 1] + nums2[idx_2], idx_1 + 1, idx_2))
                seen.add((idx_1 + 1, idx_2))

            if idx_2 + 1 < len(nums2) and (idx_1, idx_2 + 1) not in seen:
                heapq.heappush(min_heap, (nums1[idx_1] + nums2[idx_2 + 1], idx_1, idx_2 + 1))
                seen.add((idx_1, idx_2 + 1))
        
        return res


if __name__ == "__main__":
    solu = Solution()
    print(solu.kSmallestPairs([1, 1, 2], [1, 2, 3], 10))