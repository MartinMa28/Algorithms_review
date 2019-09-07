class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        num_to_idx = {}

        for idx, n in enumerate(nums):
            bucket = num_to_idx.get(n, [])
            bucket.append(idx)
            num_to_idx[n] = bucket

        for num in num_to_idx:
            if len(num_to_idx[num]) > 1:
                # appears at least twice
                for i in range(len(num_to_idx[num]) - 1):
                    if num_to_idx[num][i + 1] - num_to_idx[num][i] <= k:
                        return True


        return False