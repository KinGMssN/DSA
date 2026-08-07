import math
class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        def build(req, size):
            res=[]
            for f in range(9,1,-1):
                while req%f==0:
                    req//=f
                    res.append(str(f))
            if len(res)<size:
                res+=['1']*(size-len(res))
            return "".join(res[::-1])
        
        if self.checker(t) == True:
            return "-1"

            
        n=len(num)
        rem=[0]*(n+1)
        rem[0]=t
        for i in range(n):
            if num[i]=='0':
                break
            rem[i+1]=rem[i]//math.gcd(rem[i],int(num[i]))
        if rem[-1]==1:
            return num


        z=num.find('0')
        start=z if z!=-1 else n-1

        for i in range (start,-1,-1):
            es=n-1-i
            for d in range(int(num[i])+1,10):
                last=build(rem[i]//gcd(rem[i],d),es)
                if len(last) == es:return num[:i]+str(d)+last
        
        return build(t,n+1)

        
    

    def checker(self,n: int) -> bool:
        if n <= 1:
            return False
        
        for prime in [2,3,5,7]:
            while n % prime == 0:
                n //= prime
                
        return n > 1
        