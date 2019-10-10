class Solution:
    def merge(self, intervals: list) -> list:
        sorted_intervals = sorted(intervals)

        idx = 0
        while idx < len(sorted_intervals) - 1:
            start, end = sorted_intervals[idx]
            next_start, next_end = sorted_intervals[idx + 1]

            if end >= next_start:
                # overlaps with next range
                sorted_intervals.pop(idx)
                if end < next_end:
                    sorted_intervals[idx] = (start, next_end)
                else:
                    sorted_intervals[idx] = (start, end)

            else:
                # if does not overlap, check the next range
                idx += 1

        return sorted_intervals


if __name__ == "__main__":
    solu = Solution()
    print(solu.merge([[1,3],[2,6],[8,10],[15,18]]))