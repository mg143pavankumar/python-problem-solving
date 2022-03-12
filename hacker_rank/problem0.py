'''
    counting the number of same substrings are present in a string

    Example: 
    ABCDCDCD
    CD

    o/p: 3

'''


def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1

    return count


string = "ABCDCDCD"
sub_string = "CD"

print(count_substring(string, sub_string))
