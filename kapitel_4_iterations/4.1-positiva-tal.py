# Skriv ett program som läser in ett godtyckligt antal positiva tal
# När användaren skriver in ett negativt tal ska programmet skriva
# ut det största och det minsta av talen.

numbers = []
while True:
    number = int(input("Skriv ett positivt tal, (<0 avslutar): "))
    if number < 0:
        print(f'Min: {min(numbers)}')
        print(f'Max: {max(numbers)}')
        break
    else:
        numbers.append(number)
