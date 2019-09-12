class Solution:
    def __init__(self):
        self.combns = []
        self.num_to_letter = {'2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']}


    def _backtrack(self, digits: str, cur_comb: str) -> None:
        if len(digits) == 0:
            self.combns.append(cur_comb)
        else:
            for l in self.num_to_letter[digits[0]]:
                self._backtrack(digits[1:], cur_comb + l)


    def letterCombinations(self, digits: str) -> list:
        if len(digits) == 0:
            return []
        
        self._backtrack(digits, '')
        combinations = self.combns
        self.combns = []

        return combinations


if __name__ == "__main__":
    solu = Solution()
    print(solu.letterCombinations('23'))
    print(solu.letterCombinations('23'))