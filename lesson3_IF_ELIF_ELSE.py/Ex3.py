work_hours = int(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly pay rate: "))

if work_hours <= 40:
    gross_pay = work_hours * hourly_rate
else:
    gross_pay = (work_hours - 40) * hourly_rate * 1.5 + (40 * hourly_rate)
print("The gross pay is: $" , format(gross_pay, ".2f"))