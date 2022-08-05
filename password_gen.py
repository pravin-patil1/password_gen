""" 
    This is a basic password generator program based on user requirement. 
    * Accept password lenght from user
    * Accept number of characters, Number of digits equired in random password from user
    * Accept choice of special character from user based on @ ~ _ symbols
"""
import random,string

sp_l = ['@', '~', '_']
print('====================================')
print('   Welcome to password generator')
print('====================================\n')

lengh = int(input('Enter Password Lenght : '))
alpha =int(input('Enter No of Characters needs to be included : '))
no =int(input('Enter No of Digits needs to be included : '))
spl = int (input('Enter No of special characters required in password : '))
l_pwd = []
pwd = ''
sm = alpha+no+spl
if lengh == sm:
    for i in range(alpha):
        l_pwd.append(random.choice(string.ascii_letters))
    for y in range(no):
        l_pwd.append(random.choice(string.digits))
    for z in range(spl):
        l_pwd.append(str(random.choice(sp_l)))
    random.shuffle(l_pwd)
    for num in l_pwd:
        pwd=pwd+num
    print('Random Password : ',pwd)
else:
    print('\U0001F61E Please enter correct password lenght \U0001F61E\nPassword Lenght and no of characters, digits and special chaacters not matching!!')

