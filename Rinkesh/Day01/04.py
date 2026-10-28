import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
    
print("Setup complete ✔")
answer = 6 * 8          # oops, we wanted six times seven
check(answer, 42)