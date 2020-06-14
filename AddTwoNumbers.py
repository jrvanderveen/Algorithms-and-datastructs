#####
# Input      : heads of two linked lists representing numbers in reverse order
# Output     : return the head node of a linked listed representing the sum of both numbers
# Constraint : Lists are non empty, none negative, no leading zeros
# Edge cases :
#####


'''
As we move through each list we will have to add potentially 3 number:
    - Value from the first list
    - Value from the second list
    - Remainder from previous values


This means we will need to keep adding values to the return list until:
    - All values from list one are exhausted 
    - All values from list two are exhausted 
    - There is no remainder

So we can keep looping until each condition above has been meet.
After each iteration we will set the return list next value to the sum % 10.
We can set the remainder to the number // 10.

'''


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Num 1
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = None

# Num 2
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6
node6.next = None
###############


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        headNode = ListNode(None, None)
        node = headNode
        val = 0
        while l1 or l2 or val > 0:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            node.next = ListNode(val % 10)
            node = node.next
            val = val // 10
        return headNode.next


print("")
returnHead = Solution().addTwoNumbers(node1, node4)
while returnHead:
    print(returnHead.val)
    returnHead = returnHead.next
