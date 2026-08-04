class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        l=[]
        for sublist in grid:
            for element in sublist:
                l.append(element)
        
        grid.clear()
        
        l=self.shift(l,m*n,k)

        for i in range(0,m*n,n):
            grid.append(l[i:i+n])
        
        return grid


    def shift(self,l,length,k):
        k=k%length
        if k!=0:
            o=l[-1:]+l[0:length-1]
            return self.shift(o,length,k-1)
        else:
            return l



        