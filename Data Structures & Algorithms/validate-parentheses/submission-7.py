class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. Understand 
            - input: a string of parentheses (), {}, [] can be balanced or not
            balanced - {}
            unbalanced - ([}}
            - output: a boolean either True or False 
            - logic: Take the string (the closed parentheses) and when you get a open parentheses\
            pop it from the stack. Keep going until you go through the whole stack or don't find a match
            


        2. Plan 
            - initialize stack
            - initialize dictionary with parentheses
            - loop through the characters in the string
            - if character is open/closed parenthese add to stack
            
            - use a second if statement to check whether the open/closed parenthese
            is in stack, this time if so pop it from the stack
            - if the element you popped is not in balance with the parenthese return false
            - if not keep going all the way until you go through each character


        3. Implementation 
        '''


        stack = []
        p_dict = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            if char == ')' or char == '}' or char == ']':
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped not in p_dict[char]:
                    return False
        return not stack

        