import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
word="Mississippi"
s_count=word.count("s")
ss_count=word.count("ss")
first_ss=word.find("ss")
shouty=word.upper()
check(s_count, 4)
check(ss_count, 2)
check(first_ss, 4)
check(shouty, "MISSISSIPPI")