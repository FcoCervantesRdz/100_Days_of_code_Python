print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? : $"))
tip_percentage = int(input("How much would you like to tip? 10, 12 or 15?: "))
people = int(input("How many people to split tha bill?: "))
payment = round(total_bill*(1+tip_percentage/100)/people,2)
print(f"Each person will pay: ${payment}")