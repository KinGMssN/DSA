class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while(1):
            p=1
            x=n
            while x>0:
                p=p*(x%10)
                x=x//10
            if p%t==0:
                return n
            else:
                n=n+1
            