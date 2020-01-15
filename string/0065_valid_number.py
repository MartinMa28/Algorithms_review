class Solution:
    
    @staticmethod
    def _only_digits(s):
        if s:
            digits = set(map(lambda num: str(num), range(10)))

            for ch in s:
                if ch not in digits:
                    return False

            return True
        else:
            return False
    
    def _is_integer(self, s):
        if s:
            if s[0] in ('+', '-'):
                s = s[1:]
            
            return self._only_digits(s)
        else:
            return False
    
    def _is_float(self, s):
        if self._is_integer(s):
            return True
        
        if s:
            if s[0] in ('+', '-'):
                s = s[1:]
            
            splitted_dot = s.split('.')
            if len(splitted_dot) != 2:
                return False
            elif splitted_dot[0] and splitted_dot[1]:
                return self._only_digits(splitted_dot[0]) and\
                        self._only_digits(splitted_dot[1])
            elif splitted_dot[0]:
                return self._only_digits(splitted_dot[0])
            elif splitted_dot[1]:
                return self._only_digits(splitted_dot[1])
            else:
                return False
               
    
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if 'e' in s:
            splitted_e = s.split('e')
            
            if len(splitted_e) != 2:
                return False
            else:
                return self._is_float(splitted_e[0]) and\
                        self._is_integer(splitted_e[1])
        else:
            return self._is_float(s)
        
        
                    

def _is_integer(s_num):
    if s_num:
        if s_num[0] in ('+', '-'):
            s_num = s_num[1:]

        if s_num:
            return validate_num(s_num) and s_num[0] != '0'
        else:
            return False
    else:
        return False

def validate_num(s_num):
    if not s_num:
        return False

    digits_set = set([str(n) for n in range(10)])

    for ch in s_num:
        if ch not in digits_set:
            return False

    return True