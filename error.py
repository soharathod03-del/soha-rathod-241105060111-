print("Restaurant Billing")

items = int(input("Enter number of dishes: "))
i = 0
total = 0

while i < items:
price = int(input("Enter dish price: "))
total = total + price

if price > 500:
print("Premium dish")
else:
print("Regular dish")

i = i + 1

service = total * 10 / 100
grand_total = total + service

print("Total:", total)
print("Service Charge:", service)
print("Grand Total:", grand_total)

if grand_total > 3000:
print("High bill")
else:
print("Normal bill")

