class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        start = 0
        output = ""

        rng = int(len(s) / k)
        if len(s) % k != 0:
            rng += 1

        for iter in range(rng):
            end = (iter + 1) * k
            if end > len(s):
                end = len(s)
            if iter % 2 == 0:
                temp_str = s[start:end][::-1]
            else:
                temp_str = s[start:end]
            iter += 1
            output += temp_str
            start = end

        return output

s = Solution()
print(s.reverseStr("abcdefgh", 3))