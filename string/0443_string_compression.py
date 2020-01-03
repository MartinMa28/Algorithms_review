class Solution:
    def compress(self, chars: list) -> int:
        """
        aaaabccc
        """
        cur_idx = 0
        write = 0
        
        prev = None
        repeat = 0
        
        i = 0
        
        for i, ch in enumerate(chars):
            if ch == prev:
                repeat += 1
            else:
                if repeat >= 2:
                    for s_num in list(str(repeat)):
                        chars[write] = s_num
                        write += 1
                
                chars[write] = ch
                write += 1
                prev = ch
                repeat = 1
                
        if repeat >= 2:
            for s_num in list(str(repeat)):
                chars[write] = s_num
                write += 1
                
        return write