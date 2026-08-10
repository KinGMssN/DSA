class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dp(r):
            if r==0: return False
            
            for i in range(1,isqrt(r)+1):
                if not dp(r-i**2): return True

            return False
        return dp(n)
        