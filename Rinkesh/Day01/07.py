import sys

sys.path.insert(0, "../src")
from course_tools import check, check_output
    
print("Setup complete ✔")
printed_value = None
check(printed_value, 40, hint="Cell 2 doubles price each time it runs. Run it twice.")