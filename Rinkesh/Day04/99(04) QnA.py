import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
text="stressed"
reverse_text=text[::-1]
check(reverse_text, "desserts")