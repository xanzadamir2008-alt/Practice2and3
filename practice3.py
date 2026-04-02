# Practice 3 — Variant D — Café Bill

# ===== Task D1 — Café Info (tuple) =====
cafe_info = ("Brew & Bite", "Astana, Mangilik El 1", "Good food, great vibes")

print("=" * 30)
print(cafe_info[0])
print(cafe_info[1])
print(cafe_info[2])
print("=" * 30)

# ===== Task D2 — Order List (list) =====
items = []
prices = []

while True:
    item = input("\nEnter item name (or 'done' to finish): ")
    if item == "done":
        break
    price = float(input("Enter price: "))
    items.append(item)
    prices.append(price)

print()
print("------------------------------")
print("Your order (" + str(len(items)) + " items):")
print("------------------------------")
for i in range(len(items)):
    print(items[i], prices[i], "KZT")
print("------------------------------")

# ===== Task D3 — Unique Drinks (set) =====
unique_drinks = set()

while True:
    drink = input("\nEnter drink name (or 'done' to finish): ")
    if drink == "done":
        break
    unique_drinks.add(drink)

print()
print("Unique drinks today:", len(unique_drinks))
print(unique_drinks)

# ===== Task D4 — Bill Summary (dict) =====
customer = input("\nEnter customer name: ")
hour = int(input("Enter current hour (0-23): "))

subtotal = sum(prices)

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
    exit()

discount_amount = subtotal * discount_percent / 100
tip = (subtotal - discount_amount) * 0.1
total = subtotal - discount_amount + tip

bill = {
    "customer": customer,
    "items": len(items),
    "subtotal": subtotal,
    "discount": discount_amount,
    "tip": tip,
    "total": total
}

print()
print("=" * 30)
print("BILL -", cafe_info[0])
print("=" * 30)
print("Customer :", bill["customer"])
print("Items :", bill["items"])
print("------------------------------")
for i in range(len(items)):
    print(items[i], prices[i], "KZT")
print("------------------------------")
print("Subtotal :", bill["subtotal"], "KZT")
print("Discount :", bill["discount"], "KZT", "(" + discount_label, str(discount_percent) + "%)")
print("Tip (10%) :", bill["tip"], "KZT")
print("Total :", bill["total"], "KZT")
print("=" * 30)
