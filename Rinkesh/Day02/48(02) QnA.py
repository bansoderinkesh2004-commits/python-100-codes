price = 10
quantity = 3
total = price * quantity
price = 20          # the price changes...
print(total)        # ...but total was calculated once, already
total = price * quantity
print(total)