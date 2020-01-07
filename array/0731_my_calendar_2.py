class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for event in self.overlaps:
            if event[0] < end and start < event[1]:
                return False
        
        for event in self.calendar:
            if event[0] < end and start < event[1]:
                self.overlaps.append((max(start, event[0]), min(end, event[1])))
        
        self.calendar.append((start, end))
        
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)