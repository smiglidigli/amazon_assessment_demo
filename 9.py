class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = 0
        result_string = ''
        end = len(s)

        if len(s) == 1:
            return s

        for start in range(len(s)):
            for ix in range(start, end):
                if self.is_palindromic(s[start:ix + 1]):
                    if len(s[start:ix + 1]) > result:
                        result = len(s[start:ix + 1])
                        result_string = s[start:ix + 1]
            if end - start < result:
                break
        return result_string

    def is_palindromic(self, s):
        length = int(len(s) / 2)
        if length == 0:
            length = 1
        print("s:" + s[0:length])
        print("reverse: " + str(list(reversed(s[-length]))))
        if s[0:length] == list(reversed(s[-length])):
            return True
        else:
            return False

s = Solution()
print(s.longestPalindrome('abba'))