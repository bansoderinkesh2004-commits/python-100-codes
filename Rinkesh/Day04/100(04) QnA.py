import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
date="2026-10-29"
year=date[:4]
month=date[5:7]
day=date[8:10]
uk_date=day+"/"+month+"/"+year
check(year, "2026")
check(month, "10")
check(day, "29")
check(uk_date, "29/10/2026")
