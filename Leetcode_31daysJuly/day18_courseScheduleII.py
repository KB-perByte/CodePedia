class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { n: [] for n in range(numCourses) }
        visited = { n: 0 for n in range(numCourses) }
        result = []
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        for node in range(numCourses):
            if visited[node] == 0: 
                self.dfs(node, graph, visited, result)
                
        return result if len(result) == numCourses else []
    
    def dfs(self, node: int, graph: dict, visited: dict, result: List[int]) -> bool:
        visited[node] = 1
        
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                if not self.dfs(neighbor, graph, visited, result):
                    return False
            elif visited[neighbor] == 1:
                return False

        visited[node] = 2
        result.insert(0,node)
        
        return True 