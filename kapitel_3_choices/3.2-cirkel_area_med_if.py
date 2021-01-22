'''
beräkna cirkel area och omkrets, med test om användaren matar in <= 0 lång radie
'''
errVal = 'Du måste ange ett positivt numeriskt värde!\nFörsök igen.'

while True:
    r = input('Ange cirkelns radius i cm: ')
    if r.lower() != 'q':
        try:
            float(r)
            is_float = True
        except:
            print(errVal)
            continue
        if is_float == True:
            r = float(r)
            if r > 0:
                pi = 3.1415927
                area = pi * r**2
                omkr = pi * 2*r
                print(f'Cirkeln har en radius på {r:.2f} cm.\n\
                        Cirkeln har en omkrets på {omkr:.2f} cm.\n\
                        Cirkeln har en area på {area:.2f} cm².')
                break
            else:
                print(errVal)
    else:
        break
