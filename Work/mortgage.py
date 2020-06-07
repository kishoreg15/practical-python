# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        this_payment = payment + extra_payment
    else:
        this_payment = payment
    
    if principal > this_payment:
        principal = principal * (1+rate/12) - this_payment
        total_paid = total_paid + this_payment
    else:
        total_paid = total_paid + principal
        principal = 0
    #print(months, total_paid, principal)
    print(f'Months: {months:3d} Paid: {total_paid:10.2f} Principal: {principal:10.2f}')

print('Total paid', total_paid)