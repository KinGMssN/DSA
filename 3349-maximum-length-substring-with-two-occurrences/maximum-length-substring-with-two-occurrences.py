class Solution:
    def maximumLengthSubstring(self, nums: str) -> int:
        n, cnt = len(nums), 0
        freq = defaultdict(int)
        l = 0
        
        for r in range(n):
            x = nums[r]
            freq[x] += 1
            
            while freq[x] > 2:
                freq[nums[l]] -= 1
                l += 1
                
            cnt = max(cnt, r - l + 1)
            
        return cnt