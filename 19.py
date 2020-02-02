class Solution:
    """
    use recursion:

    keep one counter for the level of depth of the parentheses: l
    keep one counter for the number of parentheses entered overall: k

    opening a new bracket increments both k and l (we enter a new bracket pair and we go down one level)
    closing a bracket decrements only l (we go up one level, but we aren't entering a new bracket pair)

    recursion terminates when k == n (we used the requested number of brackets) and l == 0 (we closed all brackets that we opened)

    """

    def p(self, s, k, l):
        # stop recursion
        if k == self.n and l == 0:
            return {s}

        # init
        out = set()

        # if possible, open a new bracket, increment both k and l
        if k < self.n:
            out.update(self.p(s + '(', k + 1, l + 1))

        # if necessary, close a bracket, only decrement l
        if l > 0:
            out.update(self.p(s + ')', k, l - 1))

        return out

    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        return sorted(self.p('', 0, 0))