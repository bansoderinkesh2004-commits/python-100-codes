import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
name="Rinkesh"
age=22
sentence=f"{name} is {age} years old and will be {age + 1} next year."
check(sentence, "Rinkesh is 22 years old and will be 23 next year.")