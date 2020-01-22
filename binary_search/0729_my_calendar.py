class MyCalendar:

    def __init__(self):
        self.meetings = []

    def book(self, start: int, end: int) -> bool:
        '''
        [10, 20], [15, 25], [20, 30]
        '''
        idx = bisect.bisect_left(self.meetings, (start, end))
        if idx > 0:
            if self.meetings[idx - 1][1] > start:
                return False
        
        if idx < len(self.meetings):
            if self.meetings[idx][0] < end:
                return False
        
        self.meetings.insert(idx, (start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)