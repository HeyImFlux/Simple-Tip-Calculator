def calculate_tip(bill,percent):
    tip = bill * (percent / 100)
    return tip

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("what percent do you want to tip? 55"))

tip = calculate_tip(bill, tip_percent)
total = bill + tip

print(f"The tip amount is: ${tip}")
print(f"The total amount to pay is: ${total}")