# beräkna kostnaden för att ringa med en mobiltelefon med ett enkelt abonnemang.
# Programmet ska läsa in hur många minuter man ringer per månad och hur mycket
# det kostar per minut. Man får 10% rabatt om man ringer för minst 300kr.

minuter = int(input('Ange minuter: '))
taxa = float(input('Ange taxa i kr: '))
kostnad = minuter * taxa

if kostnad >= 300:
    kostnad * 0.9

print(f'Du har ringt för {kostnad:.2f} kronor denna månaden')

