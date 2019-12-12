def count_min_jumps_top_down(jumps):
    memo = {}

    def _top_down(jumps):
        t_jumps = tuple(jumps)
        if t_jumps in memo:
            return memo[t_jumps]

        if len(jumps) <= 1:
            return 0

        step = jumps[0]
        min_step = float('inf')

        for i in range(1, step + 1):
            min_step = min((min_step, _top_down(jumps[i:])))

        memo[t_jumps] = min_step + 1
        return min_step + 1

    return _top_down(jumps)
  

def count_min_jumps(jumps):
    dp = [float('inf')] * len(jumps)
    dp[0] = 0

    for i in range(len(jumps)):
        for step in range(1, jumps[i] + 1):
            if i + step < len(dp):
                dp[i + step] = min((dp[i + step], dp[i] + 1))


    return dp[-1]

def main():

  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()