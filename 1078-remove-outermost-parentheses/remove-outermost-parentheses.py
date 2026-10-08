class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r,o=[],0
        for e in s:
            if e=="(" and o > 0:
                r.append(e)
            if e==")" and o > 1:
                r.append(e)
            o+=1 if e=="(" else -1
        return "".join(r)

            
        