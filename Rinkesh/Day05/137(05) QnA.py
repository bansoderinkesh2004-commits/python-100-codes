import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
amount = 1234567.891
share=0.4567
user_id=42
number=10
money = f"${amount:,.2f}"
percent = f"{share:.2%}"
padded_id=f"{user_id:0>6}"
binary=f"{number:b}"
check(money, "$1,234,567.89")
check(percent, "45.67%")
check(padded_id, "000042")
check(binary, "1010")