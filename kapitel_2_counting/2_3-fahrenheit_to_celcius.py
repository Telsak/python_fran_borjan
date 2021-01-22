'''
Omvandlar från Fahrenheit till Celcius
'''

f_deg = float(input('Ange temperatur i Fahrenheit: '))
c_deg = (f_deg - 32) * (5 / 9)
print(f'{f_deg:.2f}\u00B0F blir {c_deg:.2f}\u00B0C')
