class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Understand:
        - An invalid list of courses is a cycle
        - Return a non-cyclic path if possible that reaches all courses
        Edge cases:
        [0,1][1,0] -> []     
        Match:
        - DFS with a stack or topological sort
        - Adjacency list 
        Plan:
        - Create a dict course to prereq by iterating through num courses and prereqs
        - Create a list of courses of the stack
        - Detect if there's a cycle per each course and it's prereqs
        - If the course has already been seen in the current stack, it's a cycle
        - If the course has no more prereqs, we can take it! it's good to go
        - If the course has prereqs, we need to see if it's a cycle
        - Add it to the current stack
        - for each prereq, check if the prereq is not in a cycle
        - if one is, we return false
        - if we can traverse, we check the next
        - if we can traverse all, we've successfully avoided a cycle, remove from current stack
        """
        prereqs = {} # key: course number, val: prereq course number
        taken = set()
        result = []

        # Create an adjacency list of courses
        for i in range(numCourses):
            prereqs[i] = []  
        for pair in prerequisites:
            prereqs[pair[0]].append(pair[1])

        currentStack = []
        def isNotCycle(course):
            if course in currentStack:
                return False
            
            if prereqs[course] == []:
                if course not in taken:
                    result.append(course)
                    taken.add(course)
                return True

            currentStack.append(course)
            for prereq in prereqs[course]:
                if isNotCycle(prereq) == False:
                    return False
            currentStack.pop()
            prereqs[course] = []
            if course not in taken:
                result.append(course)
                taken.add(course)
            return True

        for i in range(numCourses):
            if isNotCycle(i) == False:
                return []
        return result


            
            