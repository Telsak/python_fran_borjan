# Skriv ett program som skriver ut en tabell för talen 1 till 12.
# På varje rad i tabellen ska talet visas liksom talet i kvadrat
# och talet i kubik.
print(f'{"Number":^10} - {"Squared":^10} - {"Kubed":^10}')
for i in range(1, 13):
    print(f'{(i):^10} - {(i)**2:^10} - {(i)**3:^10}')
