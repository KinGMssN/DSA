class Solution:
    def reverseDegree(self, s: str) -> int:
        a=0
        for i in range(len(s)):
            p=(1+i)*(27-(ord(s[i])-96))
            a+=p
        return a
        