'''
   String validation  
'''

string = "qA2"

for test in ["isalnum", "isalpha", "isupper", "islower", "isdigit"]:
    print(any(eval("c." + test + "()") for c in string))
