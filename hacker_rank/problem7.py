
'''
    Converting lowercase letter to uppercase and vice-versa
'''

myString  = 'HackerRank.com presents "Pythonist 2".' 

print("".join([i.lower() if i.isupper() else i.upper() for i in myString]))
    