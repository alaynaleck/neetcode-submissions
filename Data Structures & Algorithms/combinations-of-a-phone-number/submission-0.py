class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # initialize results
        # for each digit, iterate through its possible letters
        # results with option 1 appended, results with option 2 appended, results with option 3 appended : cat all, send to next stage
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl", 
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        for digit in digits:
            if digit not in letters:
                return []

        results = [""]

        for digit in digits:
            new_results = []
            for letter in letters[digit]:
                for result in results:
                    new_results.append(result + letter)
            results = new_results
            
        return results

            

