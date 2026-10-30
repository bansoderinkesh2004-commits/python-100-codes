import sys
sys.path.insert(0, "../src")
from course_tools import check, check_output
item1,price1= "Coffee",3.50
item2,price2= "Bagel",2.25
print(f"{' RECEIPT ':=^21}")
print(f"{item1:<15}${price1:>5.2f}")
print(f"{item2:<15}${price2:>5.2f}")
print("-" * 21)
total = price1 + price2
print(f"Total          ${total:>5.2f}")