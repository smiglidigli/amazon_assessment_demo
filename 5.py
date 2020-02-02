class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letter_logs = []
        digit_logs = []

        for log in logs:
            first_space_index = log.find(' ')
            log_trimmed = log[first_space_index:].replace(' ', '')
            if log_trimmed.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda x: x[x.find(' ') + 1:] + x[0:x.find(' ')])
        print(letter_logs)

        return letter_logs + digit_logs

s = Solution()
s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"])