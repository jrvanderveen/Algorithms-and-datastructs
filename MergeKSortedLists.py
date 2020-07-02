#####
# Input      : List of k sorted linked lists
# Output     : Head node of a single sorted list containing all input lists
# Constraint : None
# Edge cases : Single list in array or no lists
#####

'''
This can be solved with a heapq of tuples where we sort on the node value and save the index of the list
    if there is nothing in the q return nothing, if there is only one item in the q then only one sorted list so return that node

Now we can pop from our q (pop the smallest node value) and add it to our return list.
    since we saved the list index we update the head node of the list to be node.next.  If this node is none then we do nothing else add to the q

The logic above will be reapeated until we have iterated through all the lists and popped everything from the q

N == number of nodes in list of lists
With this method we itterate through each list node one time (O(N)) and add each node to the heap (O(N*log(N))) so over all our time complexity is O(N*log(N))
    note: our heap will only ever be size len(lists) so our insertions to the q so you complxity can range from worst O(N*log(N)) to best O(N) only one list or [[1,2,3,4],[5,6,7,8]] no overlapping ranges
We are creating a new list with N values and our q will only store len(lists) so our space complexity is O(N)
'''
import heapq
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        headNodeQueue = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(headNodeQueue, (lists[i].val, i))

        if len(headNodeQueue) == 0:
            return None
        if len(headNodeQueue) == 1:
            return lists[heapq.heappop(headNodeQueue)[1]]

        returnHead = ListNode()
        node = returnHead
        while len(headNodeQueue) > 0:
            val, index = heapq.heappop(headNodeQueue)
            node.next = ListNode(val)
            node = node.next
            lists[index] = lists[index].next
            if lists[index] != None:
                heapq.heappush(headNodeQueue, (lists[index].val, index))

        return returnHead.next