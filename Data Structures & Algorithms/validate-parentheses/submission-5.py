class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            
            if char == ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped != dictionary[char]:
                    return False
        return not stack
                
           

        

        