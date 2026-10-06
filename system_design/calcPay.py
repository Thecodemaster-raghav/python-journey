# function for calculating the pay for the workers.
# cnvert hours to minutes to calculate the exact hours_worked by user
# edge cases: pay = 1.5 x base for overtime and 
# for national holiday shift pay = 1.5 x base if it goes to overtime it is stacked on top like 30 x 1.5 = 45

def calc_pay(shift_hours, hourly_pay, break_time, is_holiday):
    paid_hours = shift_hours - (break_time / 60)
    regular_hours = min(paid_hours, 8)
    overtime = max(paid_hours - 8, 0)
    if is_holiday:
        hourly_pay = hourly_pay * 1.5
    pay = regular_hours * hourly_pay + overtime * hourly_pay * 1.5 
    return pay

user_pay = calc_pay(10, 20, 30, False)
print(user_pay)