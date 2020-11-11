'''
3 mobilabbonemang: 
Kontant är bäst till högst 33 min/månad
Normal är bäst mellan 33 och 66 min/månad
Plus är bäst 66+
'''
min = 0
while min >= 0:
    min = int(input('Hur många minuter brukar du ringa? '))
    if min > 66:
        # do something
        print('Du borde välja abbonemanget Plus!')
        break
    elif 33 < min < 66:
        # do something
        print('Du borde välja abbonemanget Normal!')
        break
    elif 0 < min < 33:
        # do something
        print('Du borde välja abbonemanget Kontant!')
        break
    else:
        print('Du måste skriva ett positivt heltal!')

