
from typing import List

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

where,
1 =>I
5 => V
10 => X
50 => L
100 => C
500 => D
1000 => M

'''

# Example
'''
    input: 4
    output: "IV"
'''

# implementation for solution


def intToRoman(num: int):

    digits = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romanDigit = ["I", "IV", "V", "IX", "X", "XL",
                  "L", "XC", "C", "CD", "D", "CM", "M"]

    i = len(digits) - 1
    roman = []

    while i >= 0 and num > 0:
        if num < digits[i]:
            i = i - 1
        else:
            roman.append(romanDigit[i])
            num = num - digits[i]
    return "".join(roman)


# Taking input from the user
# intValue = int(input("Enter a number: "))
# print(f"{intValue} => {solution.intToRoman(intValue)}")


# Test cases
tests = []

# case -1
tests.append({
    "input": 5,
    "output": "V"
})

# case - 2
tests.append({
    "input": 0,
    "output": -1
})

# case - 3
tests.append({
    "input": 1,
    "output": "I"
})

# case - 4
tests.append({
    "input": 500,
    "output": "D"
})

# case - 5
tests.append({
    "input": 900,
    "output": "CM"
})

# case - 5
tests.append({
    "input": 1100,
    "output": "MC"
})


# test_all_cases(intToRoman, tests)

def test_all_cases(testCases):

    totalPassCases = 0
    totalFailCases = 0

    for i in range(len(testCases)):
        result = intToRoman(testCases[i]["input"])

        if result == testCases[i]["output"] or result == "":
            print(f"Test - {i}: Passed")
            totalPassCases = totalPassCases + 1
        else:
            print(f"Test - {i}: Faild")
            totalFailCases = totalFailCases + 1

    print(
        f"\nTotal passed cases: {totalPassCases} \t Total failed cases: {totalFailCases}")


test_all_cases(tests)
