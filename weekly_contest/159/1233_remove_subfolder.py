class Solution:
    def _split(self, path):
        return path.split('/')[1:]
    
    def _reform(self, fl):
        ret = ''
        for f in fl:
            ret += '/' + f
        
        return ret
    
    def _compare_path(self, path1, path2):
        if path1 == []:
            return True
        else:
            if path1[0] == path2[0]:
                return self._compare_path(path1[1:], path2[1:])
            else:
                return False
    
    def removeSubfolders(self, folder: list) -> list:
        folder = sorted(folder)
        folder = list(map(self._split, folder))
        left = [True for _ in range(len(folder))]
        
        for i in range(len(folder) - 1):
            for j in range(i + 1, len(folder)):
                if self._compare_path(folder[i], folder[j]):
                    left[j] = False
                else:
                    break
        
        res = []
        
        for i in range(len(folder)):
            if left[i]:
                res.append(self._reform(folder[i]))
                
        return res
        