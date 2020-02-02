class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """

        list_of_results = [0 for item in range(f)]

        if d == 1:
            return 1

        for throws in range(d):
            for ix, face in enumerate(list_of_results):
                for face2 in range(1, f + 1):
                    result = face + face2
                    if result <= target:
                        list_of_results[face2 - 1] += result
                    else:
                        list_of_results = list_of_results[0: face2 - 1]
                        break
        return len(list_of_results)

s = Solution()
s.numRollsToTarget(2, 6, 7)