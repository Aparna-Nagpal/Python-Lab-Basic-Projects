"""
One-time Passwords (OTP) is a password that is valid for only one login session or 
transaction in a computer or a digital device. Now a days OTP’s are used in almost every service like 
Internet Banking, online transactions, etc. They are generally combination of 4 or 6 numeric digits or 
a 6-digit alphanumeric. 
"""
import random
import string
print("Welcome!\nWhat length of your OTP you wish to generate?")
n=int(input())
a=int(input("if you want only numeric OTP, Type 1 \nIf you want alphanumeric OTP, Type 2\n"))
if(a==1):
    t=string.digits
    p=random.choices(t,k=n)
else:
    t=string.digits+string.ascii_lowercase+string.ascii_uppercase+'_'
    p=random.choices(t,k=n)
print(f"OTP={''.join(p)}")
