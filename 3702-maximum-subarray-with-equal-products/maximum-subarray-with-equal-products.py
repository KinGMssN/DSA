import math 
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        i=0
        j=0
        m1=2
        pv=1
        while j<len(nums):
            while math.gcd(pv,nums[j])>1:
                pv//=nums[i]
                i+=1
            pv*=nums[j]
            j+=1
            m1=max(m1,j-i)
            
        return m1




