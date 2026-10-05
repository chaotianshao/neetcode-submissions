class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp1 = {'(':')', '{':'}', '[':']'}
        mp2 = {')':'(', '}':'{', ']':'['}

        for char in s:
            if char in mp1:
                stack.append(char) 
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != mp2[char]:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

                