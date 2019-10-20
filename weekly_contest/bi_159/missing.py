class Solution:
    def missingNumber(self, arr: list) -> int:
        delta = arr[-1] - arr[0]
        delta = delta / (len(arr) + 1 - 1)
        
        for i in range(0, len(arr) - 1):
            if arr[i + 1] - arr[i] != delta:
                return int((arr[i + 1] + arr[i]) / 2)
            

if __name__ == "__main__":
    solu = Solution()
    print(solu.missingNumber([5,7, 9,13,15,17]))