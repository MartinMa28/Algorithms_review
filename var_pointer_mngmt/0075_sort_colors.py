class Solution:
    def sortColors(self, nums: list) -> None:
        # the correct place for any 2 - blue color
        blue_cursor = len(nums) - 1
        # the correct place for any 0 - red color
        red_cursor = 0

        check = 0

        while check <= blue_cursor:
            if nums[check] == 2:
                # Swap the 2 (blue) to where it's supposed to be.
                nums[check], nums[blue_cursor] = nums[blue_cursor], nums[check]
                blue_cursor -= 1
            elif nums[check] == 0:
                # Swap the 0 (red) to the correct spot
                if check != red_cursor:
                    nums[check], nums[red_cursor] = nums[red_cursor], nums[check]
                red_cursor += 1
                check += 1
            else:
                # if meet 1 (white), check next number
                check += 1


if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0]
    solu = Solution()
    solu.sortColors(colors)
    print(colors)

