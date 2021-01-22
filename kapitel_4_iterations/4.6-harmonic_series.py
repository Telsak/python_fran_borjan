# Skriv ett program som beräknar summan 1/1 - 1/2 + 1/3 - 1/4 + ...
# Upprepningen ska avslutas när den sista termen man lagt till har ett
# absolutbelopp som är mindre än 0.00001

sum = 0
i = 1
while True:
    if i % 2 == 0:
        sum -= 1/i
    else:
        sum += 1/i
#    print(1/i)
    if 1/i < 0.00001:
        print(f'sum {sum:.10f} 1/i {(1/i):.10f}')
        break
    i += 1
