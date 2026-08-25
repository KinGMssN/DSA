class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        t=True
        i=1
        n=0
        while t:
            if k*i in nums:
                i=i+1
            else:
                break
        return k*i
