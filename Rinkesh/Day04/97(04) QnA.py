import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
two_lines = "Line1\nLine2"
column="A\tB\tC"
check(two_lines, "Line1\nLine2")
check(column, "A\tB\tC")
