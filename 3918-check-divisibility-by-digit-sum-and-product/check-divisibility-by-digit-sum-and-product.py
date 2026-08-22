class Solution:
    def checkDivisibility(self, n: int) -> bool:
        p=1
        s=0
        cn=n
        while cn>0:
            r=cn%10
            p*=r
            s+=r
            cn=cn//10
        c=(n%(s+p)==0)
        return c
            
        