#####
# Input      : list of connections representing an undirected graph and num nodes
# Output     : a list of critical edges
# Constraint : at least one node and at least n-1  connections
# Edge cases : just one node then []
#####

'''
Need to create an directed graph fisrt
need a visted array / low time array of size n-1
    start at a random node but we can always start at 0 
    keep a counter and update the visted time and low time as we DFS through the graph
    once returning from the dfs check to see if the neighbor you just visted has higher low time
        if so then found a critical connection
    if not then update the low time 

This algorithm only visits each node one time so can be run in O(N)
'''
from collections import defaultdict
n1 = 4
connections1 = [[0, 1], [1, 2], [2, 0], [1, 3]]


class Solution(object):
    def criticalConnections(self, n, connections):
        def dfsGraph(time, node, parent):
            lowTime[node] = time
            vistedTime[node] = time
            visited[node] = True

            for neighbor in dGraph[node]:
                if neighbor == parent:
                    continue
                if not visited[neighbor]:
                    dfsGraph(time+1, neighbor, node)
                    lowTime[node] = min(lowTime[node], lowTime[neighbor])

                    if vistedTime[node] < lowTime[neighbor]:
                        criticalConnection.append([node, neighbor])

                else:
                    lowTime[node] = min(lowTime[node], lowTime[neighbor])

        if n == 1:
            return []
        if n == 2:
            return connections

        dGraph = defaultdict(list)
        for connection in connections:
            dGraph[connection[0]].append(connection[1])
            dGraph[connection[1]].append(connection[0])

        visited = [False for i in range(n)]
        vistedTime = [0 for i in range(n)]
        lowTime = [0 for i in range(n)]
        criticalConnection = []

        dfsGraph(0, 0, None)  # time = 0, node = 0, parent = none

        return criticalConnection


print(Solution().criticalConnections(n1, connections1))
