class Solution:
    @staticmethod
    def _is_integer(s) -> bool:
        if s[0] in ('+', '-'):
            s = s[1:]
        
        return s.isdecimal()
    
    @staticmethod
    def _is_decimal(s) -> bool:
        if s[0] in ('+', '-'):
            s = s[1:]
        
        if s.isdecimal():
            return True
        
        splitted_dot = s.split('.')
        
        if len(splitted_dot) != 2:
            return False
        elif splitted_dot[0] and splitted_dot[1]:
            return splitted_dot[0].isdecimal() and splitted_dot[1].isdecimal()
        elif not splitted_dot[0] and splitted_dot[1]:
            return splitted_dot[1].isdecimal()
        elif splitted_dot[0] and not splitted_dot[1]:
            return splitted_dot[0].isdecimal()
        else:
            return False
        
            
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if not s:
            return False
        elif 'e' in s:    
            splitted_e = s.split('e')
            
            if len(splitted_e) != 2:
                return False
            elif splitted_e[0] and splitted_e[1]:
                return self._is_decimal(splitted_e[0]) and self._is_integer(splitted_e[1])
            else:
                return False
        else:
            return self._is_decimal(s)

def _is_integer(s_num):
    pass

def validate_num(s_num):
    pass