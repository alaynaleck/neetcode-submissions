class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Create an adjacency list of courses and their prereqs
        courses = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            courses[course].append(prereq)

        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if courses[course] == []:
                return True

            visited.add(course)
            for prereq in courses[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            courses[course] = []
            return True

        for course in courses.keys():
            if not dfs(course):
                return False
                
        return True
