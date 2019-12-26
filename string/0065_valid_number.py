class Solution:
    def _is_decimal(self, s):
        if not s:
            return False
        
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        if s.isdecimal():
            return True
        
        s = s.split('.')
        
        if len(s) == 2:
            if s[0].isdecimal() and s[1].isdecimal():
                return True
            elif s[0] == '' and s[1].isdecimal():
                return True
            elif s[0].isdecimal() and s[1] == '':
                return True
            else:
                return False
        else:
            return False
    
    def _is_integer(self, s):
        if s:
            if s[0] in ('-', '+'):
                return s[1:].isdecimal()
            else:
                return s.isdecimal()
        else:
            return False
    
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if self._is_decimal(s):
            return True
        else:
            s = s.split('e')
            if len(s) == 2 and self._is_decimal(s[0]) and self._is_integer(s[1]):
                return True
            else:
                return False