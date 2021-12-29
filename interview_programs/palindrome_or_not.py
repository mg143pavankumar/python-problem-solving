'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
    For example, 121 is a palindrome while 123 is not.

'''

# Example-1
'''
input: 121
output: True
'''

# Example-2
'''
input: -121
output: False
'''

# implementation for the solution


class Solution:
    def isPalindrome(seld, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])


# Taking input the  user
num = int(input("Enter a number to check weather it is palindrome or not: "))

# Creating object of above class
solution = Solution()
print(f"Is {num} is palinedrome?: {solution.isPalindrome(num)}")
