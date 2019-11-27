class Solution:

    def maximum_ribbon_cut_top_down(self, ribbons, total):
        if total == 0:
            return 0
        elif total < 0:
            return -float('inf')
        else:
            max_cuts = -float('inf')
            for r in ribbons:
                if total - r >= 0:
                    max_cuts = max((max_cuts, 
                                self.maximum_ribbon_cut(ribbons, total - r)))
            
        return max_cuts + 1

    def maximum_ribbon_cut_bottom_up(self, ribbons, total):
        dp = [-float('inf') for _ in range(total + 1)]
        dp[0] = 0

        for i in range(1, total + 1):
            max_cuts = -float('inf')
            for r in ribbons:
                if i - r >= 0:
                    max_cuts = max((max_cuts, dp[i - r]))

            dp[i] = max_cuts + 1

        if dp[-1] == -float('inf'):
            return -1
        
        return dp[-1]


if __name__ == "__main__":
    solu = Solution()
    print(solu.maximum_ribbon_cut_bottom_up([3, 5, 7], 13))
    print(solu.maximum_ribbon_cut_bottom_up([2, 3, 5], 5))
    print(solu.maximum_ribbon_cut_bottom_up([2, 3], 7))
    print(solu.maximum_ribbon_cut_bottom_up([3, 5, 7], 13))
    print(solu.maximum_ribbon_cut_bottom_up([3, 5], 7))