import unittest


def test_all_cases(method, testCases):

    totalPassCases = 0
    totalFailCases = 0

    for i in range(len(testCases)):
        result = method(testCases[i]["input"])

        if result == testCases[i]["output"] or result == "":
            print(f"Test - {i}: Passed")
            totalPassCases = totalPassCases + 1
        else:
            print(f"Test - {i}: Faild")
            totalFailCases = totalFailCases + 1

    print(
        f"\nTotal passed cases: {totalPassCases} \t Total failed cases: {totalFailCases}")


def greeting(message, name):
    print(f"Hello! {name}")
    print(message)
