class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        numerals = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}

        subtractions = {'I': ['V', 'X'],
                        'X': ['L', 'C'],
                        'C': ['D', 'M']}

        value = 0

        ix = 0
        while ix < len(s):
            if ix + 1 < len(s) \
                    and s[ix] in subtractions.keys() \
                    and s[ix + 1] in subtractions[s[ix]]:
                value += numerals[s[ix + 1]] - numerals[s[ix]]
                ix += 2
            else:
                value += numerals[s[ix]]
                ix += 1

        return value

s = Solution()
s.romanToInt('IV')