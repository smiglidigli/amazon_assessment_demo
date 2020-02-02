class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_array = []

        for item in nums:
            if len(sorted_array) == 0:
                sorted_array.append(item)
            else:
                for ix in range(len(sorted_array)):
                    if item > sorted_array[ix]:
                        if ix == len(sorted_array) - 1:
                            sorted_array.append(item)
                        continue
                    else:
                        sorted_array.insert(ix, item)

        first_run = 1
        for ix, item in enumerate(sorted_array):
            if item > 0:
                if item != 1 and first_run:
                    return 1
                else:
                    if ix + 1 == len(sorted_array):
                        return item + 1
                    elif sorted_array[ix + 1] - item > 1:
                        return item + 1
                first_run = 0
        else:
            return 1


s = Solution()
print(s.firstMissingPositive([0]))