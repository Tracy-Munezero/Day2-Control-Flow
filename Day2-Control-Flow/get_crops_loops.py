crops=[]
while True:
    cropName= input("Please enter crop name: ")
    if cropName.lower()== 'stop':
        break
    yieldValue= float(input("Please enter yield in kg for : "))
    pricePerKg= float(input("Please enter price per kg for : "))
    totalRevenue= yieldValue * pricePerKg
    print(f"total revenue: {cropName}: {totalRevenue:.2f}")