class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        ans=0
        for i in s:
            if i =='(':
                stack.append('(')
            elif i == ')':
                stack.pop()
            ans=max(ans,len(stack))
        return ans
            


        