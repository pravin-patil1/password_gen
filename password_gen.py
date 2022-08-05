""" 
    This is a basic password generator program based on user requirement. 
    * Accept password lenght from user
    * Accept number of characters, Number of digits equired in random password from user
    * Accept choice of special character from user based on @ ~ _ symbols
"""
from pwd_gen import pwd_gen


print('=======================================')
print('+ !!Welcome to Password Generator!!  +')
print('=======================================\n')
lengh = int(input('Enter Password Lenght : '))
alpha =int(input('Enter No of Characters needs to be included : '))
no =int(input('Enter No of Digits needs to be included : '))
spl = int (input('Enter No of special characters required in password : '))
n_r = int (input('Enter Number of random passwods requireds :'))
pwd_gen(lengh,alpha,no,spl,n_r)