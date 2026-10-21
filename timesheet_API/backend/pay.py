# decimal is used for database queries so there is no error state.

from decimal import Decimal, ROUND_HALF_UP

def calc_pay(shift_hours, hourly_rate, break_time, is_holiday):
    break_time = Decimal(break_time)
    shift_hours = Decimal(str(shift_hours))
    hourly_rate = Decimal(str(hourly_rate))
    paid_hours = shift_hours - (break_time / 60)
    regular_hours = min(paid_hours, 8)
    overtime = max(paid_hours - 8, 0)
    if is_holiday:
        hourly_rate = hourly_rate * Decimal("1.5")
    pay = (regular_hours * hourly_rate + overtime * 
           hourly_rate * Decimal("1.5")).quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)
    return pay