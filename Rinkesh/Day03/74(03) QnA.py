import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
principal = 1000
rate_percent = 5
years = 10
amount = principal * (1 + rate_percent / 100) ** years
balance = 10
amount=1628.89
balance=1157.625
check(amount, 1628.89)
check(balance, 1157.625)