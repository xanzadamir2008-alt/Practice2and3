# Practice 2 — Variant D — Café Bill

# ===== Task D1 — Multiple Orders (while loop) =====
customer_name = input("Enter customer name: ")

items_count = 0
subtotal = 0.0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    subtotal += price
    items_count += 1

print()
print("Customer :", customer_name.upper())
print("Items :", items_count)
print("Subtotal :", subtotal, "KZT")

# ===== Task D2 — Time-Based Discount (if/elif/else) =====
hour = int(input("\nEnter current hour (0-23): "))

print()
print("------------------------------")

if 6 <= hour < 12:
    discount_label = "Morning discount"
    discount_percent = 10
elif 12 <= hour < 17:
    discount_label = "No discount"
    discount_percent = 0
elif 17 <= hour < 22:
    discount_label = "Evening discount"
    discount_percent = 5
else:
    print("Cafe is closed")
    print("------------------------------")
    exit()

discount_amount = subtotal * discount_percent / 100
after_discount = subtotal - discount_amount
tip = after_discount * 0.1
total = after_discount + tip

print("Time period :", discount_label)
print("Discount :", discount_amount, "KZT")
print("Tip (10%) :", tip, "KZT")
print("Total :", total, "KZT")
print("------------------------------")

# ===== Task D3 — Name Analysis (strings) =====
print()
print("Name uppercase :", customer_name.upper())
print("Name lowercase :", customer_name.lower())
print("Name length :", len(customer_name))

if customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")
