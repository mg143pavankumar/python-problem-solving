'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
'''

# Example-1
'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# implementation for solution


# List of random numbers
from typing import List
nums = [2, 5, 8, 7, 6, 3, 1, 5, 7]

# Taking target from the user
target = int(input("Enter a target value: "))


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


# Creating object
solution = Solution()

# Calling the twoSum function
postionList = solution.twoSum(nums, target)

# Displaying the result
print(f"Position list: {postionList}")
