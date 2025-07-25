class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if (i in d):
                stack.append(i)
            else:                
                if len(stack) == 0: return False
                if d[stack[-1]] != i:
                    return False               
                stack.pop()
        return len(stack) == 0
            

            
        
