class Solution:
    def checkValidString(self, s: str) -> bool:
        # from left to right
        # In this case, rule out the extra closing parentheses.
        # Note that all of asterisks are in front of the detected extra closing
        # parentheses, so these asterisks could compensate for the lack of opening paren.
        # However, in the contrary, if an asterisk wants to compensate for the lack of closings,
        # it should reside on the right of the extra opening brackets. When scanning from left
        # to right, it's hard (probably not impossible though) to keep track of the number of
        # asterisks that are on the right of opening brackets.
        open_counter = 0
        close_counter = 0
        asterisk_counter = 0

        for ch in s:
            if ch == '*':
                asterisk_counter += 1
            elif ch == '(':
                open_counter += 1
            else:
                close_counter += 1
            
            if close_counter > open_counter + asterisk_counter:
                return False

        # from right to left
        # When scanning from right to left, we are finding extra opening brackets.
        open_counter = 0
        close_counter = 0
        asterisk_counter = 0
        for ch in reversed(s):
            if ch == '*':
                asterisk_counter += 1
            elif ch == '(':
                open_counter += 1
            else:
                close_counter += 1
            
            if open_counter > close_counter + asterisk_counter:
                return False
        
        return True


if __name__ == "__main__":
    solu = Solution()
    print(solu.checkValidString("(*)("))
