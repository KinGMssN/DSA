class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c=0
        n=0
        for i in arr1:
            for j in arr2:
                if abs(i-j)<=d:
                    c=1
            if c==0:
                n+=1
            else:
                c=0

        return n