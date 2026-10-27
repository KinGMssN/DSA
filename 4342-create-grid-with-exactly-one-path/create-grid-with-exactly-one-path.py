class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + [".".rjust(n, "#")] * (m - 1) 

                    