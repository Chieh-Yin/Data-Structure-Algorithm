class Solution:
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while (k**2 + k)/2 <= n:
            k = k+1
        return k-1
        
