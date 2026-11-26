class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        elif n<19:
            return True
        elif n<27:
            return False
        elif n<34:
            return True
        elif n < 40:
            return False
        elif n< 45:
            return True
        elif n< 49:
            return False
        else:
            return True


        