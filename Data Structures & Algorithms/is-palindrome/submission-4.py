class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for char in s:
            if char.isalnum():
                new_string += char

        print(new_string)

        left = 0
        right = len(new_string) - 1

        while left <= right:
            if new_string[left].lower() != new_string[right].lower():
                return False
            left += 1
            right -= 1
        return True
        