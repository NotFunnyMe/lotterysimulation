import random
account = 0

for i in range(30):
    bet = random.randint(1,10)
    lucky_draw = random.randint(1,10)
    print("bet : ",bet)
    print("lucky draw : ",lucky_draw)

    if lucky_draw == bet:
        account = account+10000-1000
    else:
        account = account-1000
        print("Your current balance is $",account)