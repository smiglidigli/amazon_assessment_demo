class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        bin_x = "{0:08b}".format(x)
        bin_y = "{0:08b}".format(y)

        print(bin_x)
        print(bin_y)

        len_x = len(bin_x)
        len_y = len(bin_y)
        min_len = min(len_x, len_y)
        diff = abs(len_x - len_y)

        hamming_distance = 0

        for ix in range(1, min_len + 1):
            if not bin_x[-ix] == bin_y[-ix]:
                hamming_distance += 1

        if len_x > len_y:
            hamming_distance += sum([int(v) for v in bin_x[0:diff]])
        elif len_y > len_x:
            hamming_distance += sum([int(v) for v in bin_y[0:diff]])

        return hamming_distance

s = Solution()
s.hammingDistance(1, 40000)