class Solution:
    def isValid(self, s: str) -> bool:
        b_dict = {'}': '{', ']': '[', ')': '('}
        
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    popped = stack.pop()
                    if popped != b_dict[char]:
                        return False
        return not stack
                        