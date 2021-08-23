# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def append(curr, s):
            s += str(curr.val)
            if curr.next != None:
                ret_s = ''
                ret_s = append(curr.next, s)
                return ret_s
            return s
        
        l1_num = int(append(l1, ''))
        l2_num = int(append(l2, ''))
        out = str(l1_num+l2_num)
        
        def re_list(s):
            ln = ListNode(0, None)
            curr = ln
            for num in range(len(s)):
                curr.val = s[num]
                if num < len(s) - 1:
                    curr.next = ListNode(0, None)
                    curr = curr.next
            return ln

        return re_list(out)
