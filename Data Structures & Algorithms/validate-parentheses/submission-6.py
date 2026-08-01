class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. Understand (input/output, edge cases, potential tradeoffs)
            -Given a set of characters ({[]}) in a string and need to determine whether
            the set of parentheses are balanced or not
            - Example: [] = balanced, [{}) = not balanced
            - Usage of stack. push open brackets and pop closed brackets
            - empty string

        2. Plan 
            -create dictionary containing all characters
            - loop through characters in the string 
            - create a stack array
            - if any of them are the open parentheses, append them into stack
            - continuing with the conditionals, if any are closed parentheses, pop
            whatever is in the stack, (make a variable out of it) if that value is not in the 
            dictionary return false, else keep iterating through list

        3. Implement

        '''

        stack = []
        my_dict = {'}': '{', ']': '[', ')': '('}


        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            if char == '}' or char == ']' or char == ')':
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if popped != my_dict[char]:
                    return False
        return not stack




        