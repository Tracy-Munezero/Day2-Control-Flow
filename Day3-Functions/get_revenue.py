def calculate_revenue(yield_value, price_per_kg):
  total_revenue = yield_value * price_per_kg
  return total_revenue

cropName= input("Enter crop name: ")
yieldValue= float(input(f"Enter yield in kg: "))
pricePerKg = float (input("Enter price per kg: "))

total_revenue = calculate_revenue(yieldValue, pricePerKg)
print(f"Total Revenue for {cropName}: {total_revenue:.2f}")
