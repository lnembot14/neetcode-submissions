class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) != 0:
                    popped = stack.pop()
                    if popped == p_dict[char]:
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack


        
        