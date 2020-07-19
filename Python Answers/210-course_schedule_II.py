class Solution:

    def findOrder(self, numCourses, prerequisites):

        self.res = []
        self.graph = collections.defaultdict(list)
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1])

        self.visited = [0] * numCourses

        for x in range(numCourses):
            if not self.DFS(x):
                return []
                # continue to search the whole graph
        return self.res


    def DFS(self, node):
        # cycle detected
        if self.visited[node] == -1: 
            return False
        # has been finished, and been added to self.res
        if self.visited[node] == 1:
            return True 
        # mark as visited
        self.visited[node] = -1 
        for x in self.graph[node]:
            if not self.DFS(x):
                return False
        # mark as finished
        self.visited[node] = 1
        # add to solution as the course depenedent on previous ones 
        self.res.append(node) 
        return True
        