import time

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums = list(set(nums))

        nums.sort()

        print(nums)

        output = []

        first_number = 1

        while first_number < nums[0]:
            output.append(first_number)
            first_number += 1

        for ix in range(len(nums) - 1):
            rng = nums[ix + 1] - nums[ix]

            for ix2 in range(rng - 1):
                output.append(nums[ix] + ix2 + 1)

        return output

s = Solution()
start_time = time.time()
for i in range (1000):
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))

print("--- %s seconds ---" % (time.time() - start_time))