from collections import deque

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def _binary_search(self, arr: list, val: int) -> int:
        """
        Find the index of target value, if not found return -1.
        """
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == val:
                return mid, True
            elif arr[mid] > val:
                right = mid - 1
            else:
                left = mid + 1

        return mid, False

    
    def findClosestElements(self, arr: list, k: int, x: int) -> list:
        if x < arr[0]:
            return arr[:k]

        if x > arr[-1]:
            return arr[-k:]
        
        x_idx, found = self._binary_search(arr, x)
        
        res = deque()
        if found:
            res.append(arr[x_idx])
            # node = ListNode(arr[x_idx])
            # left_header = node
            # right_header = node
            go_left = x_idx - 1
            go_right = x_idx + 1
        else:
            go_left = x_idx - 1
            go_right = x_idx
            if (x - arr[go_left]) > (arr[go_right] - x):
                # if two sides are of the same length, then choose from the left side
                # node = ListNode(arr[go_right])
                # left_header = node
                # right_header = node
                res.append(arr[go_right])
                go_right += 1
            else:
                # node = ListNode(arr[go_left])
                # left_header = node
                # right_header = node
                res.append(arr[go_left])
                go_left -= 1

        length = 1
        while length < k:
            if go_left >= 0 and go_right < len(arr):
                if (x - arr[go_left]) > (arr[go_right] - x):
                    # new_node = ListNode(arr[go_right])
                    # right_header.right = new_node
                    # new_node.left = right_header
                    # right_header = right_header.right
                    res.append(arr[go_right])
                    go_right += 1
                    length += 1
                else:
                    # new_node = ListNode(arr[go_left])
                    # left_header.left = new_node
                    # new_node.right = left_header
                    # left_header = left_header.left
                    res.appendleft(arr[go_left])
                    go_left -= 1
                    length += 1
            else:
                if go_left < 0:
                    # new_node = ListNode(arr[go_right])
                    # right_header.right = new_node
                    # new_node.left = right_header
                    # right_header = right_header.right
                    res.append(arr[go_right])
                    go_right += 1
                    length += 1
                
                if go_right == len(arr):
                    # new_node = ListNode(arr[go_left])
                    # left_header.left = new_node
                    # new_node.right = left_header
                    # left_header = left_header.left
                    res.appendleft(arr[go_left])
                    go_left -= 1
                    length += 1

        # res = []
        # while left_header:
        #     res.append(left_header.val)
        #     left_header = left_header.right
        
        return res
            
            


if __name__ == "__main__":
    solu = Solution()

    print(solu.findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4))
        