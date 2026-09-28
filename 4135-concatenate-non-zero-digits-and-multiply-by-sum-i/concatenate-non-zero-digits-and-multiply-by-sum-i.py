class Solution:
    def sumAndMultiply(self, n: int) -> int:
        c=1
        x=0
        s=0
        while n>0:
            r=n%10
            if r!=0:
                x=x+r*(10**c)
                c=c+1
                s=s+r
            n=n//10
        return (s*x)//10

                
        