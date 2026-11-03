class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        s=0
        for i in nums:
            s=s+m-i
        return s
        