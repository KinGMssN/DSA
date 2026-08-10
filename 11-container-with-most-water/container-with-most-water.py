class Solution:
    def maxArea(self, towers: List[int]) -> int:
        n=len(towers)
        l=0
        r=n-1
        mw=-1
        while(l<r):
            w=min(towers[l],towers[r])*(r-l)
            mw=max(mw,w)
            if towers[l]<towers[r]:
                l+=1
            else:
                r-=1
        return mw
        