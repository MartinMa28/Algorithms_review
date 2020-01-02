class Solution:
    def reorderLogFiles(self, logs: list) -> list:
        
        letter_logs = []
        digit_logs = []
        
        for l in logs:
            identifier, parsed = l.split(' ', 1)
            if parsed[0].isdecimal():
                digit_logs.append((parsed, identifier))
            else:
                letter_logs.append((parsed, identifier))
                
        letter_logs.sort()
        
        return [' '.join((l[1], l[0])) for l in letter_logs + digit_logs]