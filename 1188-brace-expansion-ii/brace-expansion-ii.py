class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        idx = 0
        n = len(expression)

        def is_letter(c: str) -> bool:
            return "a" <= c <= "z"

        def expr() -> set:
            nonlocal idx
            ret = set()
            while True:
                ret |= term()
                if idx < n and expression[idx] == ",":
                    idx += 1
                    continue
                else:
                    break
            return ret

        def term() -> set:
            nonlocal idx
            ret = {""}
            while idx < n and (
                expression[idx] == "{" or is_letter(expression[idx])
            ):
                sub = item()
                tmp = set()
                for left in ret:
                    for right in sub:
                        tmp.add(left + right)
                ret = tmp
            return ret

        def item() -> set:
            nonlocal idx
            ret = set()
            if expression[idx] == "{":
                idx += 1
                ret = expr()
            else:
                ret = {expression[idx]}
            idx += 1
            return ret

        ret = expr()
        return sorted(list(ret))