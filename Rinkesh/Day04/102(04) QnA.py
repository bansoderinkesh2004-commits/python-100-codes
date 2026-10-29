import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
typo="Pxthon"
fixed=typo[:1]+"y"+typo[2:]
check(fixed, "Python")