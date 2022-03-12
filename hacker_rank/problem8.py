'''
    split and join the string
    
    Example: 
    a = "This is one example"

    a = "This-is-one-example"
'''


def split_join_line(line):
    return "-".join(line.split(" "))


a = "This is one example"
print(split_join_line(a))