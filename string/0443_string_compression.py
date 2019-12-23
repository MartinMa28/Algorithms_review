class Solution:
    def compress(self, chars: list) -> int:
        if len(chars) == 1:
            return 1
        
        length = len(chars)
        cnt = 1
        prev_ch = chars.pop(0)
        occur = 1
        
        while cnt < length:
            if chars[0] == prev_ch:
                occur += 1
                chars.pop(0)
            else:
                chars.append(prev_ch)
                
                if occur > 1:
                    chars.extend(list(str(occur)))
                
                prev_ch = chars[0]
                occur = 1
                chars.pop(0)
            
            cnt += 1
        
        chars.append(prev_ch)
        if occur > 1:
            chars.extend(list(str(occur)))
            
        
        return len(chars)