'''
omvandla från miles/gallon till kilometer/liter
'''

mpg = float(input('Ange miles per gallon (mpg): '))
        
km = mpg * 1.609
liter = 3.785

print(f'{km / liter:.2f}')
