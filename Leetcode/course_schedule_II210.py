class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            ans = []
            for i in range(numCourses):
                ans.append(i)
            return ans

        adj_list = {}
        visited = {}

        for a, b in prerequisites:
            if not adj_list.get(b):
                adj_list[b] = []
            adj_list[b].append(a)

        def isDAG(node):
            visited[node] = 1

            if not adj_list.get(node):
                visited[node] = 2
                return True

            for adj_node in adj_list[node]:
                if not visited.get(adj_node):
                    isDag = isDAG(adj_node)
                    if not isDag:
                        return False
                elif visited[adj_node] == 1:
                    return False
            visited[node] = 2
            return True

        # def detectCycle(node):
        #     visited[node] = 1
        #     if not adj_list.get(node):
        #         visited[node] = 2
        #         return False

        #     for adj_node in adj_list[node]:
        #         if not visited.get(adj_node):
        #             isCycleExists = detectCycle(adj_node)
        #             if isCycleExists:
        #                 return True
        #         elif visited[adj_node] == 1:
        #             return True
        #     visited[node] = 2
        #     return False

        for node, _ in adj_list.items():
            if not visited.get(node):
                isDag = isDAG(node)
                if not isDag:
                    return []

        visited.clear()

        node_stack = []

        def dfs(node):
            visited[node] = 1

            if adj_list.get(node):
                for adj_node in adj_list[node]:
                    if not visited.get(adj_node):
                        dfs(adj_node)
            node_stack.append(node)

        for node, _ in adj_list.items():
            if not visited.get(node):
                dfs(node)
        for i in range(numCourses):
            if i not in node_stack:
                node_stack.append(i)

        node_stack.reverse()
        return node_stack


obj = Solution()

# numCourses = 2
# prerequisites = [[1, 0]]

# numCourses = 4
# prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

# numCourses = 1
# prerequisites = []

numCourses = 3
prerequisites = [[1, 0]]

print(obj.findOrder(numCourses, prerequisites))
