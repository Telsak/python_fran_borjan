'''
skriv ett program som låter användaren välja 3 olika funktioner:
1. Hej, 2. Recept eller 3. Diagnosfrågor
'''

while True:
    print("\n")
    print('=========== MENY =============')
    print('Meny:\n   1. Hej\n   2. Recept\n   3. Diagnosfrågor')

    meny_svar = input('Välj alternativ 1-3:')
    try:
        num = int(meny_svar)
        if int(meny_svar) == 1:
            namn = input('\nVad heter du? ')
            print('Hej {}. Jag gillar dig!'.format(namn))
        elif int(meny_svar) == 2:
            print('\nBaka sockerkaka')
            sats = input('Ange antal satser: ')
            try:
                num = int(sats)
                print('Sockerkaka, {} sats'.format(num * 1))
                print('{} st ägg'.format(num * 3))
                print('{} dl strösocker'.format(num * 3))
                print('{} tsk vaniljsocker'.format(num * 2))
                print('{} tsk bakpulver'.format(num * 2))
                print('{} dl vetemjöl'.format(num * 3))
                print('{} g smör'.format(num * 75))
                print('{} dl vatten'.format(num * 1))
            except ValueError:
                print('Måste vara ett heltal!')
        elif int(meny_svar) == 3:
            fraga_1 = input('\nÄr du täppt i näsan? (j/n)')
            if fraga_1.lower() == 'j':
                fraga_2 = input('Har du feber? (j/n)')
                if fraga_2.lower() == 'j':
                    print('Du är förkyld. Stanna hemma och ta det lugnt!')
                else:
                    print('Du har förmodligen hösnuva Uppsök apotek!')
            else:
                print('Du är frisk. Gå och jobba eller studera!')
    except ValueError:
        print('Måste vara ett heltal!')
    input('Press enter to continue...')

