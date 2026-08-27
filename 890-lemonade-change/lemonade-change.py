class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        for i in range(len(bills)):
            if bills[i] == 5:
                change[5] += 1
            elif bills[i] == 10:
                if change[5] == 0:
                    return False
                change[5] -= 1
                change[10] += 1
            elif bills[i] == 20:
                if change[5] == 0 or (change[10] == 0 and change[5] < 3):
                    return False
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                change[20] += 1

        return True
        