class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return (min(nums1)%2 ==1 or sum(1 for x in nums1 if x%2==1)==0)
