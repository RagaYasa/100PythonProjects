print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input(f"What percentage tip would you like to give? {10} {12} {15} "))
people = int(input("How many people to split the bill? "))

per_person = bill / people
percentage = tip / 100 + 1
tip2 = percentage * bill
person_pay = tip2 / people
final_amount = (round(person_pay, 2))
final_final = round((person_pay - per_person), 2)
print(f"so the tip would be : ${final_final}")



