class Solution:
    def isPalindrome(self, s: str) -> bool:
        constructed_string = ""
        for char in s:
            if char.isalnum():
                constructed_string += char
        
        left = 0
        right = len(constructed_string) - 1

        while left < right:
            if constructed_string[left].lower() != constructed_string[right].lower():
                return False
            left += 1
            right -= 1
        return True
        