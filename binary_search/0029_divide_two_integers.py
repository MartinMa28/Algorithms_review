class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        elif divisor == 1:
            if dividend > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif dividend < -(2 ** 31):
                return -(2 ** 31)
            else:
                return dividend
        elif divisor == -1:
            if dividend > 2 ** 31:
                return -(2 ** 31)
            elif dividend < -(2 ** 31 - 1):
                return 2 ** 31 - 1
            else:
                return -dividend
        else:
            positive = True
            if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
                positive = False
                
            dividend = abs(dividend)
            divisor = abs(divisor)
            
            if dividend < divisor:
                return 0
            elif dividend == divisor:
                if positive:
                    return 1
                else:
                    return -1
            else:
                e = 2
                while dividend > divisor ** e:
                    e += 1
                    
                left = divisor ** (e - 2)
                right = divisor ** (e - 1)
                
                while left + 1 < right:
                    mid = (left + right) // 2
                    
                    if dividend >= divisor * mid:
                        left = mid
                    else:
                        right = mid
                
                if right * divisor <= dividend:
                    res = right
                else:
                    res = left
                
                if positive:
                    if res > 2 ** 31 - 1:
                        return 2 ** 31 - 1
                    else:
                        return res
                else:
                    if -res < -(2 ** 31):
                        return -(2 ** 31)
                    else:
                        return -res
                
                