class Solution:
    
    def _is_float_num(self, s: str) -> bool:
        if '.' in s:
            split_period = s.split('.')
            if len(split_period) != 2:
                return False
            else:
                if split_period[0] and split_period[1]:
                    return split_period[0].isdecimal() and \
                            split_period[1].isdecimal()
                elif split_period[0]:
                    return split_period[0].isdecimal()
                elif split_period[1]:
                    return split_period[1].isdecimal()
                else:
                    return False
        else:
            return s.isdecimal()
        
    def _is_integer(self, s):
        if s:
            if s[0] == '+' or s[0] == '-':
                s = s[1:]

                return s.isdecimal()
            else:
                return s.isdecimal()
        else:
            return False
            
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if not s:
            return False
        else:
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
                
            if s.isdecimal():
                return True
            else:
                if 'e' in s:
                    split_e = s.split('e')
                    if len(split_e) != 2 or \
                        (not self._is_float_num(split_e[0])) or\
                        (not self._is_integer(split_e[1])):
                        return False
                    else:
                        return True
                else:
                    return self._is_float_num(s)
                