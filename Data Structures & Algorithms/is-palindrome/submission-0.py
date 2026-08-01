class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([char.lower() for char in s if char.isalnum()])
        pointer_1 = 0
        pointer_2 = len(new_s)-1

        while pointer_1<pointer_2:
            if new_s[pointer_1] != new_s[pointer_2]:
                return False
            else:
                pointer_1 += 1
                pointer_2 -= 1 
        return True

        