class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. Understand 
            - input: a string, more specifically a string with spaces in between
            - output: boolean
            - core logic: taking two pointers from the left and right and seeing
            if each of the letters are equal (hence palindrome)
            - edge cases: empty string, fully non alphanumeric characters


        2. Plan 
            - manipulate the string to try and get all of it to be one string as opposed 
            to having spaces
            - initialize left and right pointers
            loop through the string 
            check if the two strings are equal keep moving both, if not return false
            return true if we've seen every character and they've all been equal


        3. Implement 
        '''

        new_string = ""
        for char in s:
            if not char.isalnum():
                pass
            else:
                new_string += char.lower()

        print(new_string)
        left = 0
        right = len(new_string) - 1 

        while left < right:
            if new_string[left] == new_string[right]:
                right -= 1
                left += 1
            else:
                return False
        return True 

        