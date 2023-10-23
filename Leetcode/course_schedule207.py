'''
class Solution(object):
    adj_list = {}
    visited = {}

    def detectCycle(self, node):
        self.visited[node] = 1
        if not self.adj_list.get(node):
            self.visited[node] = 2
            return False

        for adj_node in self.adj_list[node]:
            if not self.visited.get(adj_node):
                isCycleExists = self.detectCycle(adj_node)
                if isCycleExists:
                    return True
            elif self.visited[adj_node] == 1:
                return True
        self.visited[node] = 2
        return False

    def canFinish(self, numCourses, prerequisites):

        for a, b in prerequisites:
            if not self.adj_list.get(b):
                self.adj_list[b] = []

            self.adj_list[b].append(a)

        for node, _ in self.adj_list.items():
            if not self.visited.get(node):
                isCycleExists = self.detectCycle(node)
                if isCycleExists:
                    return False
        return True


numCourses = 2
prerequisites = [[1, 0]]
# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]
# numCourses = 4
# prerequisites = [[1, 0], [1, 2], [0, 3], [2, 0]]

obj = Solution()
print(obj.canFinish(numCourses, prerequisites))

'''


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj_list = {}
        visited = {}

        for a, b in prerequisites:
            if not adj_list.get(b):
                adj_list[b] = []

            adj_list[b].append(a)

        def detectCycle(node):
            visited[node] = 1
            if not adj_list.get(node):
                visited[node] = 2
                return False

            for adj_node in adj_list[node]:
                if not visited.get(adj_node):
                    isCycleExists = detectCycle(adj_node)
                    if isCycleExists:
                        return True
                elif visited[adj_node] == 1:
                    return True
            visited[node] = 2
            return False

        for node, _ in adj_list.items():
            if not visited.get(node):
                isCycleExists = detectCycle(node)
                if isCycleExists:
                    return False
        return True


# numCourses = 2
# prerequisites = [[1, 0]]
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
# numCourses = 4
# prerequisites = [[1, 0], [1, 2], [0, 3], [2, 0]]

obj = Solution()
print(obj.canFinish(numCourses, prerequisites))
