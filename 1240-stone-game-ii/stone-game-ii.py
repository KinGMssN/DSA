class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp={}


        def dfs(alice,i,M):
            if i==len((piles)):
                return 0
            if (alice,i,M) in dp :
                return dp[(alice,i,M)]
            r=0 if alice else float("inf")
            t=0
            for X in range(1,M*2+1,1):
                if i+X>len(piles):
                    break
                t+=piles[i+X-1]
                if alice:
                    r=max(r,t+dfs(not alice,i+X,max(M,X)))
                else:
                    r=min(r,dfs(not alice,i+X,max(M,X)))
            dp[(alice,i,M)]=r
            return r
        return dfs(True,0,1)
