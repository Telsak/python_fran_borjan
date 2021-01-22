# på ett matteprov kunde man få högst 50 poäng. Gränsen för betyget E var 25
# poäng och för betygen D, C, B och A 30, 35, 40 respektive 45 poäng.
# Skriv ett program som läser in poängen för en elev och som visar vilket
# betyg hon eller han fick på provet.

elev = input('Ange elevens namn: ')
score = float(input('Ange poäng: '))
if score >= 45:
    grade = 'A'
elif score >= 40:
    grade = 'B'
elif score >= 35:
    grade = 'C'
elif score >= 30:
    grade = 'D'
else:
    grade = 'E'

if score.is_integer():
    print(f'{elev}: Poäng {int(score)} ger betyget {grade}.')
else:
    print(f'{elev}: Poäng {score:.1f} ger betyget {grade}.')

