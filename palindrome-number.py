class Solution:
    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        n = x
        new_number = 0
        while n != 0:
            new_number = new_number * 10 + n % 10
            n = n // 10
        if x == new_number: return True
        else: return False
        

            

        
