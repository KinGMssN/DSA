class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answers = []

        def remove(text, scan_start, delete_start, opening, closing):
            balance = 0

            for i in range(scan_start, len(text)):
                if text[i] == opening:
                    balance += 1
                elif text[i] == closing:
                    balance -= 1

                if balance >= 0:
                    continue

                for j in range(delete_start, i + 1):
                    if text[j] == closing and (
                        j == delete_start or text[j - 1] != closing
                    ):
                        remove(
                            text[:j] + text[j + 1 :],
                            i,
                            j,
                            opening,
                            closing,
                        )

                return

            reversed_text = text[::-1]

            if opening == "(":
                remove(reversed_text, 0, 0, ")", "(")
            else:
                answers.append(reversed_text)

        remove(s, 0, 0, "(", ")")
        return answers