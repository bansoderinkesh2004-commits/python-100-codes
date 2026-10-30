import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
raw_email="JOHN.SMITH@EXAMPLE.COM \n"
email=raw_email.strip().lower()
username=email.split("@")[0]
domain=email.split("@")[1]
check(username, "john.smith")
check(domain, "example.com")
check(email, "john.smith@example.com")