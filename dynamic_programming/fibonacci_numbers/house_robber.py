def find_max_steal(wealth):
    dp = {}

    return _find_max_steal(tuple(wealth), dp)

def _find_max_steal(wealth, dp):
    if wealth in dp:
        return dp[wealth]

    if wealth == []:
        return 0
    elif len(wealth) == 1:
        dp[wealth] = wealth[0]
        return wealth[0]
    else:
        steal = _find_max_steal(wealth[2:], dp) + wealth[0]
        not_steal = _find_max_steal(wealth[1:], dp)

        return max((steal, not_steal))


def main():
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))


main()