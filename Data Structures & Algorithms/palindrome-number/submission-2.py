class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        # count places
        digits = 1
        while x // (10 ** digits) > 0:
            digits += 1
        
        # initialize left and right pointers to the middle digits
        left = right = math.ceil(digits / 2)
        if digits % 2 == 0: 
            left +=1 # even numbers have two middles

        while left <= digits:
            leftPlace = x % (10 ** left) // (10 ** (left - 1))
            rightPlace = x % (10 ** right) // (10 ** (right - 1))
            if leftPlace != rightPlace:
                return False
            left += 1
            right -= 1

        return True 