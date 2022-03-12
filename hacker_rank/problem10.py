'''
Wrap the string into paragraph

Example: Hellow
o/p: Hell
     ow


'''


def wrap(string, max_width):
    return "\n".join([string[i: i + max_width] for i in range(0, len(string), max_width)])


string = "Helloworld"
max_width = 4

print(wrap(string, max_width))
