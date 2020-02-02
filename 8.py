# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_linked = []
        l2_linked = []

        for ix in range(len(l1) - 1):
            temp_list = ListNode(l1[ix])
            temp_list.next = l1[ix + 1]
            l1_linked.append(temp_list)

        for ix in range(len(l2) - 1):
            temp_list = ListNode(l2[ix])
            temp_list.next = l2[ix + 1]
            l2_linked.append(temp_list)


        val1 = self.calculate_sum_of_linked_list(l1_linked)
        val2 = self.calculate_sum_of_linked_list(l2_linked)

        return val1 + val2

    def calculate_sum_of_linked_list(self, linked_list):
        value = linked_list.val
        ix = 0
        multiplier = 1
        while 1:
            try:
                multiplier *= 10
                value = linked_list.next * multiplier
                linked_list.val = linked_list.next
            except:
                break

        return value

s = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(s.addTwoNumbers(l1, l2))