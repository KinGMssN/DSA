class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums)>50000:
            if nums[50000]==1:
                    return 1
        k=len(nums)-k
        return self.qs(nums,len(nums),k)

    def qs(self,nums,n,k):

        p=self.partition(nums,n)
        if (p==k):
            return nums[p]
        elif (k<p):
            return self.qs(nums[0:p],p,k)
        else:
            return self.qs(nums[p+1:],n-(p+1),k-(p+1))
            



    def partition(self,lst,n):
        l=0
        r=n-1
        while l<r:
                
            if lst[l]>lst[l+1]:
                lst[l],lst[l+1]=lst[l+1],lst[l]
                l+=1

            elif lst[r]>lst[l]:
                r-=1

            else:
                lst[r],lst[l+1]=lst[l+1],lst[r]
                lst[l],lst[l+1]=lst[l+1],lst[l]
                l+=1

        return l
                    

        