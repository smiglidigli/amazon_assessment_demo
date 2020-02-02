class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 0:
            return False

        sum_n = 0

        print("{0:#b}".format(n))

        binary = "{0:#b}".format(n)

        for number in binary[binary.find("b") + 1:]:
            sum_n += int(number)

        if sum_n == 1:
            return True
        else:
            return False

s = Solution()
print(s.isPowerOfTwo(-16))