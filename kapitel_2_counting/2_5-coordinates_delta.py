'''
Beräkna avståndet mellan två koordinater i ett 2D system
s = sqrt((x1 - x2)² + (y1 - y2)²)
förenkla...
s = sqrt(delta_x² + delta_y³)
s = sqrt(sum_delta_squares)

(delta betyder skillnad)
'''

from math import sqrt

# Först ber vi om koordinater
x1 = float(input('Första koordinat X: '))
y1 = float(input('Första koordinat Y: '))
x2 = float(input('Andra koordinat X: '))
y2 = float(input('Andra koordinat Y: '))

# nu räknar vi lite
delta_x = x1 - x2
delta_y = y1 - y2
sum_delta_squares = delta_x**2 + delta_y**2
s = sqrt(sum_delta_squares)
print(f'Avståndet mellan koordinat {x1,y1} och {x2,y2} är {s}')
