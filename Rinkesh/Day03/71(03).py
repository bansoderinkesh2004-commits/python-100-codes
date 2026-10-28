import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
2+3*4**2/8-1
prediction=7.0
check(prediction, 7.0, hint="Do 4 ** 2 first, then * and /, left to right, then + and -. And remember that / gives a float.")