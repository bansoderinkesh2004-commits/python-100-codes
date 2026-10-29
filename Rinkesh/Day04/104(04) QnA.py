import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
s="abcdefghi"
middle=[4]
outer_removed=s[1:-1]
check(middle, "e")
check(outer_removed,"bcdefgh")