import random,string
sp_l = ['@', '~', '_']

def pwd_gen(l,c,d,s,rn):
    l_pwd = []
    pwd = ''
    lt = c+d+s
    rn_pwd =[]
    while rn > 0:
        if lt == l:
            for i in range(c):
                l_pwd.append(random.choice(string.ascii_letters))
            for y in range(d):
                l_pwd.append(random.choice(string.digits))
            for z in range(s):
                l_pwd.append(str(random.choice(sp_l)))
            random.shuffle(l_pwd)
            for num in l_pwd:
                pwd=pwd+num
            rn_pwd.append(pwd)
            pwd=''
            l_pwd=[]
        else:
            print('\U0001F61E Please enter correct password lenght \U0001F61E\nPassword Lenght and no of characters, digits and special chaacters not matching!!')
        rn -= 1
    print('=============================\nRandom Passwords as below : \n')
    for i in rn_pwd:
        print(i)
    print('\n____________________________\nThank you !!\n=============================')
    