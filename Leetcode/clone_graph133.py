from collections import defaultdict


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return node

        newNode = defaultdict()

        def cloneGraphByDFS(node):
            if node in newNode:
                return newNode[node]

            clonedNode = Node(node.val)
            newNode[node] = clonedNode
            for neighbor in node.neighbors:
                clonedNode.neighbors.append(cloneGraphByDFS(neighbor))

            return clonedNode
