class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        seen = {}
        
        def check(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j) in seen:
                return seen[(i, j)]
            
            found = False

            if i < len(s1) and s1[i] == s3[k]:
                found = check(i+1, j, k+1)

            if not found and j < len(s2) and s2[j] == s3[k]:
                found = check(i, j+1, k+1)

            seen[(i, j)] = found
            return found
    
        return check(0, 0, 0)