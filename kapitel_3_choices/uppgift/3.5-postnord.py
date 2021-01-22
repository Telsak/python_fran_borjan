'''
I postnords anvisningar finns följande föreskrifter för hur stora och små vanliga brev får vara:
Maximimått: Längd 600mm, Tjocklek 100mm, Bredd+Längd+Tjocklek högst 900 mm.
Minimimått: Längd 140mm, Bredd 90mm.
Skriv ett program som läser in ett brevs längd, bredd och tjocklek och undersöker
om brevet har tillåtna mått eller inte. Använd tecknet \ i if-satsen för att dela upp de
logiska uttrycket så det blir mer lättläst.
'''

length = int(input('Ange längd i mm: '))
width = int(input('Ange bredd i mm: '))
thick = int(input('Ange tjocklek i mm: '))

switch = " ej "
if length + width + thick <= 900 and \
        length <= 600 and \
        thick <= 100 and \
        length >= 140 and \
        width >= 90:
    switch = " "
    print('allowed')
print(f'Brevet har{switch}tillåtna dimensioner!')
