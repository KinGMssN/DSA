class Solution:
    def maxDepth(self, s: str) -> int:
        c1=0
        ans=0
        for i in s:
            if i =='(':
                c1=c1+1
            elif i == ')':
                c1=c1-1
            ans=max(ans,c1)
        return ans
            


        