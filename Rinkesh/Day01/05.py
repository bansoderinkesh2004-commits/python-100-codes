import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
    
print("Setup complete ✔")
print("Hello, world!")
check_output("Hello, world!")