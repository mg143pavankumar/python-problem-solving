'''Write a Python program to display the current date and time.'''

# solution
import datetime as dt

current_time = dt.datetime.now()

# method-1
print(current_time)

# method-2: for specific 
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))
