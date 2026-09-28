class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0 :
            return 0
        n=str(n)
        s=0
        st=''
        for i in n:
            if i != '0':
                s=s+int(i)
                st=st+i
        return int(st)*s


                
        