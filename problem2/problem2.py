'''Write a Python program to get the Python version you are using.'''

# solution
import sys
import platform

print(f"Python version => {sys.version}")
print(f"Version info => {sys.version_info}")


# method -2
print("")
print(f"Python version => {platform.python_version()}")
print(platform.python_version_tuple())
