class Solution:
    def dailyTemperatures(self, T: list) -> list:
        if len(T) == 1:
            return [0]
        else:
            mono_stack = [(T[0], 0)]
            i = 1
            res = [0] * len(T)
            
            while i < len(T):
                if T[i] <= mono_stack[-1][0]:
                    mono_stack.append((T[i], i))
                else:
                    while mono_stack:
                        if T[i] > mono_stack[-1][0]:
                            _, popped_idx = mono_stack.pop()
                            res[popped_idx] = i - popped_idx
                        else:
                            break
                            
                    mono_stack.append((T[i], i))
                
                i += 1
                    
            return res
                

if __name__ == "__main__":
    solu = Solution()
    print(solu.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))