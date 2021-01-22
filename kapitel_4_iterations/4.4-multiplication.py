# Skriv ett program som visar en multiplikationstabell. Programmet
# ska utformas så att man läser in antalet rader som ska skrivas ut.
# Tips: använd nästlade for-satser.

rader = int(input("Ange nummer (1-9): "))
for row in range(1, rader + 1):
    for col in range(1, 10):
        if col == 9:
            print(f'{(row * col):>3}')
        else:
            print(f'{(row * col):>3}', end='  ')

