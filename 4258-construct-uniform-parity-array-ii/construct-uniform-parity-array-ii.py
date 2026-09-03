class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=min(nums1)
        c=sum(1 for x in nums1 if x%2==1)
        return mn%2 ==1 or c==0
