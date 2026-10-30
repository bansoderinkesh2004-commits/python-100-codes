import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
name = input("What is your name? ")
print("Your,", name)
check_output("Hello, Ada!", inputs=["Ada"])