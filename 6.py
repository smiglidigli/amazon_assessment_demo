class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        output = []
        # output.append(type1)
        # output.append(type2)

        for ix in range(n):
            sequence_start = '('
            left = 1
            right = 0
            output.append(self.add_node(sequence_start, left + 1, right + 1, n))

        print(output)

        return output

    def add_node(self, sequence, left, right, n):
        if left > n and right > n:
            return sequence
        if left > n:
            # can`t add left
            return self.add_node([sequence + ')'], left, right + 1, n)
        elif right == left:
            # can`t add right
            return self.add_node([sequence + '('], left + 1, right, n)
        else:
            return [self.add_node([sequence + '('], left + 1, right, n),
                    self.add_node([sequence + ')'], left, right + 1, n)]

s = Solution()
s.generateParenthesis(3)