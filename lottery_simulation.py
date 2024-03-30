import random
bet = int(input("your bet from 1 to 10 : "))
lucky_draw = random.randint(1,10)
account = 0
if lucky_draw == bet:
    account = account+10000-100
else:
    account = account-100
print(lucky_draw)
print(account)