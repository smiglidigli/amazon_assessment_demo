from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt_debug = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        cnt = [key for key, v in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)]
        print(cnt_debug)
        print(cnt)

        return cnt[0:k]

s = Solution()
s.topKFrequent([1,1,1,2,2,3], 2)