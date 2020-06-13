#####
# I: head of a linked list where each node has a pointer to the next node and a pointer to a random node in the set
# O: head to a deep copy of the list
# C: -1000 <= Node.val <= 1000 num nodes < 1000
# E: can be given null for head node
#####
# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
###############
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None
###############
node1.random = None
node2.random = node6
node3.random = node5
node4.random = node4
node5.random = node3
node6.random = node2


class Solution(object):
    def copyRandomList(self, head):
        nodeDict = {}
        nodeDict[None] = None
        n = m = head
        while m:
            nodeDict[m] = Node(m.val)
            m = m.next

        while n:
            nodeDict[n].next = nodeDict[n.next]
            nodeDict[n].random = nodeDict[n.random]
            n = n.next

        return nodeDict[head]

    def copyRandomListDefaultDict(self, head):
        nodeDict = defaultdict(lambda: Node(0))
        nodeDict[None] = None
        m = head
        while m:
            nodeDict[m].val = m.val
            nodeDict[m].next = nodeDict[m.next]
            nodeDict[m].random = nodeDict[m.random]
            m = m.next


y = Solution().copyRandomList(node1)
while y:
    print("val " + str(y.val) + " random val " +
          (str(y.random.val) if y.random is not None else " none "))
    y = y.next

print("")
y = Solution().copyRandomListDefaultDict(node1)
while y:
    print("val " + str(y.val) + " random val " +
          (str(y.random.val) if y.random is not None else " none "))
    y = y.next
