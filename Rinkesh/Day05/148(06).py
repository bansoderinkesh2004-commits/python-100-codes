# 1. input
text = input("Temperature in Celsius: ")
# 2. convert
celsius = float(text)
# 3. compute
fahrenheit = celsius * 9 / 5 + 32
# 4. output
print(f"{celsius}°C is {fahrenheit:.1f}°F")