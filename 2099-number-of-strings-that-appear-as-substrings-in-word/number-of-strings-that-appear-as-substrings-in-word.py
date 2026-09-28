class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        c=0
        for i in patterns:
            if i in word:
                c=c+1
        return c
        