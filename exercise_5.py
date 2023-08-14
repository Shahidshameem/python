'''a=int(input('enter your present age in years:'))
b=int(input('enter your age in months'))
c=int(input('enter your age in weeks'))
d=int(input('enter your age in days'))
l1=90
l2=12
l3=52
l4=365
print(f'You have {l1-a}years,{l2-b}months,{l3-c}weeks and {l4-d}days left ')'''
age=int(input("enter your present age:"))
age_left=90-age
days=age_left*365
weeks=age_left*52
months=age_left*12
years=age_left
print(f"you have {days},{weeks},{months} and {years} year")