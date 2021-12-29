'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

where,
I => 1
V => 5
X => 10
L => 50
C => 100
D => 500
M => 1000

'''

# Example
'''
    input: "IV"
    output: 4
'''

# implementation for solution


class Solution:
    def romanToInt(self, s: str):
        # declaring dict of roman to int
        romanDict = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        flag = 1
        val = 0

        # Logic
        for i in range(len(s) - 1, -1, -1):
            if flag <= romanDict[s[i]]:
                val = val + romanDict[s[i]]
                flag = romanDict[s[i]]
            else:
                val = val - romanDict[s[i]]
        return val


# Creating object
solution = Solution()

# Taking roman number from the user
romanNum = str(input("Enter a roman number in capital: "))
print(f"{romanNum} => {solution.romanToInt(romanNum)}")
