class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def createCombinations(combination, index, total):
            if total == target:
                result.append(combination.copy())
                return
            if index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    return
            
                combination.append(candidates[i])
                createCombinations(combination, i + 1, total + candidates[i])
                combination.pop()

        createCombinations([], 0, 0)
        return result